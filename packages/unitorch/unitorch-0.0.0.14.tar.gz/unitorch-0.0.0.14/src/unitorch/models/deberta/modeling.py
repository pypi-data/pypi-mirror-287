# Copyright (c) FULIUCANSHENG.
# Licensed under the MIT License.

import torch
import torch.nn as nn
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union
from transformers.models.deberta.modeling_deberta import (
    DebertaConfig,
    DebertaModel,
    DebertaOnlyMLMHead,
    ContextPooler,
    StableDropout,
)
from unitorch.models import GenericModel


class DebertaForClassification(GenericModel):
    def __init__(
        self,
        config_path: str,
        num_classes: Optional[int] = 1,
        gradient_checkpointing: Optional[bool] = False,
    ):
        """
        Initializes the DebertaForClassification model.

        Args:
            config_path (str): The path to the Deberta model configuration file.
            num_classes (int, optional): The number of classes for classification. Defaults to 1.
            gradient_checkpointing (bool, optional): Whether to use gradient checkpointing for memory optimization. Defaults to False.
        """
        super().__init__()
        self.config = DebertaConfig.from_json_file(config_path)
        self.config.gradient_checkpointing = gradient_checkpointing
        self.deberta = DebertaModel(self.config)
        self.pooler = ContextPooler(self.config)
        self.dropout = StableDropout(self.config.hidden_dropout_prob)
        self.classifier = nn.Linear(self.config.hidden_size, num_classes)
        self.init_weights()

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        token_type_ids: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.Tensor] = None,
    ):
        """
        Performs forward pass of the DebertaForClassification model.

        Args:
            input_ids (torch.Tensor): The input tensor containing token ids.
            attention_mask (torch.Tensor, optional): The attention mask tensor. Defaults to None.
            token_type_ids (torch.Tensor, optional): The token type ids tensor. Defaults to None.
            position_ids (torch.Tensor, optional): The position ids tensor. Defaults to None.

        Returns:
            (torch.Tensor):The output logits tensor.
        """
        outputs = self.deberta(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
        )
        pooled_output = self.pooler(outputs[0])

        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)
        return logits


class DebertaForMaskLM(GenericModel):
    def __init__(
        self,
        config_path: str,
        gradient_checkpointing: Optional[bool] = False,
    ):
        """
        Initializes the DebertaForMaskLM model.

        Args:
            config_path (str): The path to the Deberta model configuration file.
            gradient_checkpointing (bool, optional): Whether to use gradient checkpointing for memory optimization. Defaults to False.
        """
        super().__init__()
        self.config = DebertaConfig.from_json_file(config_path)
        self.config.gradient_checkpointing = gradient_checkpointing
        self.deberta = DebertaModel(self.config)
        self.cls = DebertaOnlyMLMHead(self.config)
        self.cls.predictions.decoder.weight = (
            self.deberta.embeddings.word_embeddings.weight
        )
        self.init_weights()

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        token_type_ids: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.Tensor] = None,
    ):
        """
        Performs forward pass of the DebertaForMaskLM model.

        Args:
            input_ids (torch.Tensor): The input tensor containing token ids.
            attention_mask (torch.Tensor, optional): The attention mask tensor. Defaults to None.
            token_type_ids (torch.Tensor, optional): The token type ids tensor. Defaults to None.
            position_ids (torch.Tensor, optional): The position ids tensor. Defaults to None.

        Returns:
            (torch.Tensor):The output logits tensor.
        """
        outputs = self.deberta(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
        )
        sequence_output = outputs[0]
        logits = self.cls(sequence_output)
        return logits
