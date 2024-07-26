# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DedicatedAiClusterCapacityArgs',
    'EndpointContentModerationConfigArgs',
    'ModelFineTuneDetailsArgs',
    'ModelFineTuneDetailsTrainingConfigArgs',
    'ModelFineTuneDetailsTrainingDatasetArgs',
    'ModelModelMetricArgs',
    'GetDedicatedAiClustersFilterArgs',
    'GetEndpointsFilterArgs',
    'GetModelsFilterArgs',
]

@pulumi.input_type
class DedicatedAiClusterCapacityArgs:
    def __init__(__self__, *,
                 capacity_type: Optional[pulumi.Input[str]] = None,
                 total_endpoint_capacity: Optional[pulumi.Input[int]] = None,
                 used_endpoint_capacity: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] capacity_type: The type of the dedicated AI cluster capacity.
        :param pulumi.Input[int] total_endpoint_capacity: The total number of endpoints that can be hosted on this dedicated AI cluster.
        :param pulumi.Input[int] used_endpoint_capacity: The number of endpoints hosted on this dedicated AI cluster.
        """
        if capacity_type is not None:
            pulumi.set(__self__, "capacity_type", capacity_type)
        if total_endpoint_capacity is not None:
            pulumi.set(__self__, "total_endpoint_capacity", total_endpoint_capacity)
        if used_endpoint_capacity is not None:
            pulumi.set(__self__, "used_endpoint_capacity", used_endpoint_capacity)

    @property
    @pulumi.getter(name="capacityType")
    def capacity_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the dedicated AI cluster capacity.
        """
        return pulumi.get(self, "capacity_type")

    @capacity_type.setter
    def capacity_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capacity_type", value)

    @property
    @pulumi.getter(name="totalEndpointCapacity")
    def total_endpoint_capacity(self) -> Optional[pulumi.Input[int]]:
        """
        The total number of endpoints that can be hosted on this dedicated AI cluster.
        """
        return pulumi.get(self, "total_endpoint_capacity")

    @total_endpoint_capacity.setter
    def total_endpoint_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "total_endpoint_capacity", value)

    @property
    @pulumi.getter(name="usedEndpointCapacity")
    def used_endpoint_capacity(self) -> Optional[pulumi.Input[int]]:
        """
        The number of endpoints hosted on this dedicated AI cluster.
        """
        return pulumi.get(self, "used_endpoint_capacity")

    @used_endpoint_capacity.setter
    def used_endpoint_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "used_endpoint_capacity", value)


@pulumi.input_type
class EndpointContentModerationConfigArgs:
    def __init__(__self__, *,
                 is_enabled: pulumi.Input[bool]):
        """
        :param pulumi.Input[bool] is_enabled: (Updatable) Whether to enable the content moderation feature.
        """
        pulumi.set(__self__, "is_enabled", is_enabled)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[bool]:
        """
        (Updatable) Whether to enable the content moderation feature.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_enabled", value)


@pulumi.input_type
class ModelFineTuneDetailsArgs:
    def __init__(__self__, *,
                 dedicated_ai_cluster_id: pulumi.Input[str],
                 training_dataset: pulumi.Input['ModelFineTuneDetailsTrainingDatasetArgs'],
                 training_config: Optional[pulumi.Input['ModelFineTuneDetailsTrainingConfigArgs']] = None):
        """
        :param pulumi.Input[str] dedicated_ai_cluster_id: The OCID of the dedicated AI cluster this fine-tuning runs on.
        :param pulumi.Input['ModelFineTuneDetailsTrainingDatasetArgs'] training_dataset: The dataset used to fine-tune the model. 
               
               Only one dataset is allowed per custom model, which is split 80-20 for training and validating. You must provide the dataset in a JSON Lines (JSONL) file. Each line in the JSONL file must have the format: `{"prompt": "<first prompt>", "completion": "<expected completion given first prompt>"}`
        :param pulumi.Input['ModelFineTuneDetailsTrainingConfigArgs'] training_config: The fine-tuning method and hyperparameters used for fine-tuning a custom model.
        """
        pulumi.set(__self__, "dedicated_ai_cluster_id", dedicated_ai_cluster_id)
        pulumi.set(__self__, "training_dataset", training_dataset)
        if training_config is not None:
            pulumi.set(__self__, "training_config", training_config)

    @property
    @pulumi.getter(name="dedicatedAiClusterId")
    def dedicated_ai_cluster_id(self) -> pulumi.Input[str]:
        """
        The OCID of the dedicated AI cluster this fine-tuning runs on.
        """
        return pulumi.get(self, "dedicated_ai_cluster_id")

    @dedicated_ai_cluster_id.setter
    def dedicated_ai_cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "dedicated_ai_cluster_id", value)

    @property
    @pulumi.getter(name="trainingDataset")
    def training_dataset(self) -> pulumi.Input['ModelFineTuneDetailsTrainingDatasetArgs']:
        """
        The dataset used to fine-tune the model. 

        Only one dataset is allowed per custom model, which is split 80-20 for training and validating. You must provide the dataset in a JSON Lines (JSONL) file. Each line in the JSONL file must have the format: `{"prompt": "<first prompt>", "completion": "<expected completion given first prompt>"}`
        """
        return pulumi.get(self, "training_dataset")

    @training_dataset.setter
    def training_dataset(self, value: pulumi.Input['ModelFineTuneDetailsTrainingDatasetArgs']):
        pulumi.set(self, "training_dataset", value)

    @property
    @pulumi.getter(name="trainingConfig")
    def training_config(self) -> Optional[pulumi.Input['ModelFineTuneDetailsTrainingConfigArgs']]:
        """
        The fine-tuning method and hyperparameters used for fine-tuning a custom model.
        """
        return pulumi.get(self, "training_config")

    @training_config.setter
    def training_config(self, value: Optional[pulumi.Input['ModelFineTuneDetailsTrainingConfigArgs']]):
        pulumi.set(self, "training_config", value)


@pulumi.input_type
class ModelFineTuneDetailsTrainingConfigArgs:
    def __init__(__self__, *,
                 training_config_type: pulumi.Input[str],
                 early_stopping_patience: Optional[pulumi.Input[int]] = None,
                 early_stopping_threshold: Optional[pulumi.Input[float]] = None,
                 learning_rate: Optional[pulumi.Input[float]] = None,
                 log_model_metrics_interval_in_steps: Optional[pulumi.Input[int]] = None,
                 lora_alpha: Optional[pulumi.Input[int]] = None,
                 lora_dropout: Optional[pulumi.Input[float]] = None,
                 lora_r: Optional[pulumi.Input[int]] = None,
                 num_of_last_layers: Optional[pulumi.Input[int]] = None,
                 total_training_epochs: Optional[pulumi.Input[int]] = None,
                 training_batch_size: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] training_config_type: The fine-tuning method for training a custom model.
        :param pulumi.Input[int] early_stopping_patience: Stop training if the loss metric does not improve beyond 'early_stopping_threshold' for this many times of evaluation.
        :param pulumi.Input[float] early_stopping_threshold: How much the loss must improve to prevent early stopping.
        :param pulumi.Input[float] learning_rate: The initial learning rate to be used during training
        :param pulumi.Input[int] log_model_metrics_interval_in_steps: Determines how frequently to log model metrics. 
               
               Every step is logged for the first 20 steps and then follows this parameter for log frequency. Set to 0 to disable logging the model metrics.
        :param pulumi.Input[int] lora_alpha: This parameter represents the scaling factor for the weight matrices in LoRA.
        :param pulumi.Input[float] lora_dropout: This parameter indicates the dropout probability for LoRA layers.
        :param pulumi.Input[int] lora_r: This parameter represents the LoRA rank of the update matrices.
        :param pulumi.Input[int] num_of_last_layers: The number of last layers to be fine-tuned.
        :param pulumi.Input[int] total_training_epochs: The maximum number of training epochs to run for.
        :param pulumi.Input[int] training_batch_size: The batch size used during training.
        """
        pulumi.set(__self__, "training_config_type", training_config_type)
        if early_stopping_patience is not None:
            pulumi.set(__self__, "early_stopping_patience", early_stopping_patience)
        if early_stopping_threshold is not None:
            pulumi.set(__self__, "early_stopping_threshold", early_stopping_threshold)
        if learning_rate is not None:
            pulumi.set(__self__, "learning_rate", learning_rate)
        if log_model_metrics_interval_in_steps is not None:
            pulumi.set(__self__, "log_model_metrics_interval_in_steps", log_model_metrics_interval_in_steps)
        if lora_alpha is not None:
            pulumi.set(__self__, "lora_alpha", lora_alpha)
        if lora_dropout is not None:
            pulumi.set(__self__, "lora_dropout", lora_dropout)
        if lora_r is not None:
            pulumi.set(__self__, "lora_r", lora_r)
        if num_of_last_layers is not None:
            pulumi.set(__self__, "num_of_last_layers", num_of_last_layers)
        if total_training_epochs is not None:
            pulumi.set(__self__, "total_training_epochs", total_training_epochs)
        if training_batch_size is not None:
            pulumi.set(__self__, "training_batch_size", training_batch_size)

    @property
    @pulumi.getter(name="trainingConfigType")
    def training_config_type(self) -> pulumi.Input[str]:
        """
        The fine-tuning method for training a custom model.
        """
        return pulumi.get(self, "training_config_type")

    @training_config_type.setter
    def training_config_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "training_config_type", value)

    @property
    @pulumi.getter(name="earlyStoppingPatience")
    def early_stopping_patience(self) -> Optional[pulumi.Input[int]]:
        """
        Stop training if the loss metric does not improve beyond 'early_stopping_threshold' for this many times of evaluation.
        """
        return pulumi.get(self, "early_stopping_patience")

    @early_stopping_patience.setter
    def early_stopping_patience(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "early_stopping_patience", value)

    @property
    @pulumi.getter(name="earlyStoppingThreshold")
    def early_stopping_threshold(self) -> Optional[pulumi.Input[float]]:
        """
        How much the loss must improve to prevent early stopping.
        """
        return pulumi.get(self, "early_stopping_threshold")

    @early_stopping_threshold.setter
    def early_stopping_threshold(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "early_stopping_threshold", value)

    @property
    @pulumi.getter(name="learningRate")
    def learning_rate(self) -> Optional[pulumi.Input[float]]:
        """
        The initial learning rate to be used during training
        """
        return pulumi.get(self, "learning_rate")

    @learning_rate.setter
    def learning_rate(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "learning_rate", value)

    @property
    @pulumi.getter(name="logModelMetricsIntervalInSteps")
    def log_model_metrics_interval_in_steps(self) -> Optional[pulumi.Input[int]]:
        """
        Determines how frequently to log model metrics. 

        Every step is logged for the first 20 steps and then follows this parameter for log frequency. Set to 0 to disable logging the model metrics.
        """
        return pulumi.get(self, "log_model_metrics_interval_in_steps")

    @log_model_metrics_interval_in_steps.setter
    def log_model_metrics_interval_in_steps(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "log_model_metrics_interval_in_steps", value)

    @property
    @pulumi.getter(name="loraAlpha")
    def lora_alpha(self) -> Optional[pulumi.Input[int]]:
        """
        This parameter represents the scaling factor for the weight matrices in LoRA.
        """
        return pulumi.get(self, "lora_alpha")

    @lora_alpha.setter
    def lora_alpha(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "lora_alpha", value)

    @property
    @pulumi.getter(name="loraDropout")
    def lora_dropout(self) -> Optional[pulumi.Input[float]]:
        """
        This parameter indicates the dropout probability for LoRA layers.
        """
        return pulumi.get(self, "lora_dropout")

    @lora_dropout.setter
    def lora_dropout(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "lora_dropout", value)

    @property
    @pulumi.getter(name="loraR")
    def lora_r(self) -> Optional[pulumi.Input[int]]:
        """
        This parameter represents the LoRA rank of the update matrices.
        """
        return pulumi.get(self, "lora_r")

    @lora_r.setter
    def lora_r(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "lora_r", value)

    @property
    @pulumi.getter(name="numOfLastLayers")
    def num_of_last_layers(self) -> Optional[pulumi.Input[int]]:
        """
        The number of last layers to be fine-tuned.
        """
        return pulumi.get(self, "num_of_last_layers")

    @num_of_last_layers.setter
    def num_of_last_layers(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "num_of_last_layers", value)

    @property
    @pulumi.getter(name="totalTrainingEpochs")
    def total_training_epochs(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of training epochs to run for.
        """
        return pulumi.get(self, "total_training_epochs")

    @total_training_epochs.setter
    def total_training_epochs(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "total_training_epochs", value)

    @property
    @pulumi.getter(name="trainingBatchSize")
    def training_batch_size(self) -> Optional[pulumi.Input[int]]:
        """
        The batch size used during training.
        """
        return pulumi.get(self, "training_batch_size")

    @training_batch_size.setter
    def training_batch_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "training_batch_size", value)


@pulumi.input_type
class ModelFineTuneDetailsTrainingDatasetArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 dataset_type: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 object: pulumi.Input[str]):
        """
        :param pulumi.Input[str] bucket: The Object Storage bucket name.
        :param pulumi.Input[str] dataset_type: The type of the data asset.
        :param pulumi.Input[str] namespace: The Object Storage namespace.
        :param pulumi.Input[str] object: The Object Storage object name.
        """
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "dataset_type", dataset_type)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "object", object)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        The Object Storage bucket name.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="datasetType")
    def dataset_type(self) -> pulumi.Input[str]:
        """
        The type of the data asset.
        """
        return pulumi.get(self, "dataset_type")

    @dataset_type.setter
    def dataset_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "dataset_type", value)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        """
        The Object Storage namespace.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def object(self) -> pulumi.Input[str]:
        """
        The Object Storage object name.
        """
        return pulumi.get(self, "object")

    @object.setter
    def object(self, value: pulumi.Input[str]):
        pulumi.set(self, "object", value)


@pulumi.input_type
class ModelModelMetricArgs:
    def __init__(__self__, *,
                 final_accuracy: Optional[pulumi.Input[float]] = None,
                 final_loss: Optional[pulumi.Input[float]] = None,
                 model_metrics_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[float] final_accuracy: Fine-tuned model accuracy.
        :param pulumi.Input[float] final_loss: Fine-tuned model loss.
        :param pulumi.Input[str] model_metrics_type: The type of the model metrics. Each type of model can expect a different set of model metrics.
        """
        if final_accuracy is not None:
            pulumi.set(__self__, "final_accuracy", final_accuracy)
        if final_loss is not None:
            pulumi.set(__self__, "final_loss", final_loss)
        if model_metrics_type is not None:
            pulumi.set(__self__, "model_metrics_type", model_metrics_type)

    @property
    @pulumi.getter(name="finalAccuracy")
    def final_accuracy(self) -> Optional[pulumi.Input[float]]:
        """
        Fine-tuned model accuracy.
        """
        return pulumi.get(self, "final_accuracy")

    @final_accuracy.setter
    def final_accuracy(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "final_accuracy", value)

    @property
    @pulumi.getter(name="finalLoss")
    def final_loss(self) -> Optional[pulumi.Input[float]]:
        """
        Fine-tuned model loss.
        """
        return pulumi.get(self, "final_loss")

    @final_loss.setter
    def final_loss(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "final_loss", value)

    @property
    @pulumi.getter(name="modelMetricsType")
    def model_metrics_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the model metrics. Each type of model can expect a different set of model metrics.
        """
        return pulumi.get(self, "model_metrics_type")

    @model_metrics_type.setter
    def model_metrics_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_metrics_type", value)


@pulumi.input_type
class GetDedicatedAiClustersFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


@pulumi.input_type
class GetEndpointsFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


@pulumi.input_type
class GetModelsFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str],
                 regex: Optional[bool] = None):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "values", values)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[bool]:
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[bool]):
        pulumi.set(self, "regex", value)


