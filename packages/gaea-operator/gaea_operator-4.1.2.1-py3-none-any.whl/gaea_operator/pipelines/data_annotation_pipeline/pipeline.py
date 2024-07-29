#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/06/05
# @Author  : 李岱
# @File    : pipeline.py
"""
from paddleflow.pipeline import Pipeline
from paddleflow.pipeline import CacheOptions
from paddleflow.pipeline import ContainerStep
from paddleflow.pipeline import Artifact
from paddleflow.pipeline import ExtraFS

import os


@Pipeline(
    name="ppyoloe_plus",
    cache_options=CacheOptions(enable=False),
)
def pipeline(extra_fs_name: str = "vistudio",
             extra_fs_mount_path: str = "/home/paddleflow/storage/mnt/fs-root-vistudio",
             windmill_ak: str = "",
             windmill_sk: str = "",
             windmill_endpoint: str = "",
             experiment_kind: str = "",
             experiment_name: str = "",
             modelstore_name: str = "",
             tracking_uri: str = "",
             project_name: str = "",
             train_dataset_name: str = "",
             val_dataset_name: str = "",
             base_train_dataset_name: str = "",
             base_val_dataset_name: str = "",
             train_model_name: str = "",
             train_model_display_name: str = "",
             workspace_id: str = "",
             icafe_id: str = "",
             icafe_operator: str = ""):
    """
    Pipeline for std_algorithm training eval transform transform-eval package inference.
    """
    base_params = {"flavour": "c4m16gpu1",
                   "queue": "qtrain",
                   "windmill_ak": windmill_ak,
                   "windmill_sk": windmill_sk,
                   "windmill_endpoint": windmill_endpoint,
                   "experiment_name": experiment_name,
                   "experiment_kind": experiment_kind,
                   "tracking_uri": tracking_uri,
                   "project_name": project_name,
                   "model_store_name": modelstore_name,
                   "workspace_id": workspace_id,
                   "icafe_id": icafe_id,
                   "icafe_operator": icafe_operator}
    base_env = {"PF_JOB_FLAVOUR": "{{flavour}}",
                "PF_JOB_QUEUE_NAME": "{{queue}}",
                "WINDMILL_AK": "{{windmill_ak}}",
                "WINDMILL_SK": "{{windmill_sk}}",
                "WINDMILL_ENDPOINT": "{{windmill_endpoint}}",
                "EXPERIMENT_KIND": "{{experiment_kind}}",
                "EXPERIMENT_NAME": "{{experiment_name}}",
                "TRACKING_URI": "{{tracking_uri}}",
                "PROJECT_NAME": "{{project_name}}",
                "WORKSPACE_ID": "{{workspace_id}}",
                "PIPELINE_ROLE": "windmill",
                "ICAFE_ID": "{{icafe_id}}",
                "ICAFE_OPERATOR": "{{icafe_operator}}"}

    dataannotation_params = {"train_dataset_name": train_dataset_name,
                         "val_dataset_name": val_dataset_name,
                         "base_train_dataset_name": base_train_dataset_name,
                         "base_val_dataset_name": base_val_dataset_name,
                         "model_name": train_model_name,
                         "model_display_name": train_model_display_name,
                         "advanced_parameters": '{"epoch":"1",'
                                                '"LearningRate.base_lr":"0.00001",'
                                                '"worker_num":"1",'
                                                '"eval_size":"640*640",'
                                                '"TrainReader.batch_size":"8",'
                                                '"model_type":"ppyoloe_m"}',
                         "pdc_ak": "",
                         "pdc_sk": "",
                         "algo_id": "",
                         "train_group_name": "",
                         "k8s_gpu_cards": "",
                         "pdc_train_mirror": "",
                         "train_config_params_uri": "",
                         }
    dataannotation_env = {"TRAIN_DATASET_NAME": "{{train_dataset_name}}",
                      "VAL_DATASET_NAME": "{{val_dataset_name}}",
                      "BASE_TRAIN_DATASET_NAME": "{{base_train_dataset_name}}",
                      "BASE_VAL_DATASET_NAME": "{{base_val_dataset_name}}",
                      "MODEL_NAME": "{{model_name}}",
                      "MODEL_DISPLAY_NAME": "{{model_display_name}}",
                      "ADVANCED_PARAMETERS": "{{advanced_parameters}}",
                      "PF_EXTRA_WORK_DIR": extra_fs_mount_path,
                      "PIPELINE_ROLE": "windmill",
                      "TRAIN_CONFIG_PARAMS_URI": "{{train_config_params_uri}}"
                      }
    dataannotation_env.update(base_env)
    dataannotation_params.update(base_params)

    data_annotation = ContainerStep(name="data_annotation",
                                docker_env="iregistry.baidu-int.com/acg_aiqp_algo/paddlecloud/ubuntu18.04:cuda11.8"
                                           "-cudnn8.6"
                                           "-gaea-op8",
                                parameters=dataannotation_params,
                                env=dataannotation_env,
                                extra_fs=[ExtraFS(name=extra_fs_name, mount_path=extra_fs_mount_path)],
                                outputs={"output_model_uri": Artifact(), "output_uri": Artifact()},
                                command=f'cd /root && '
                                        f'package_path=$(python3 -c "import site; print(site.getsitepackages()[0])") '
                                        f'&& python3 -m gaea_operator.components.annotation.annotation'
                                        f'--output-model-uri={{{{output_model_uri}}}} '
                                        f'--output-uri={{{{output_uri}}}} '
                                )

    return data_annotation.outputs["output_uri"]


if __name__ == "__main__":
    pipeline_client = pipeline(
        accelerator="T4",
        windmill_ak="a1a9069e2b154b2aa1a83ed12316d163",
        windmill_sk="eefac23d2660404e93855197ce60efb3",
        windmill_endpoint="http://10.27.240.5:8340",
        experiment_kind="Aim",
        experiment_name="std_algorithm",
        tracking_uri="aim://10.27.240.5:8329",
        project_name="workspaces/internal/projects/proj-o97H2oAE",
        train_dataset_name="workspaces/internal/projects/proj-o97H2oAE/datasets/ds-UCKo4LyJ/versions/1",
        val_dataset_name="workspaces/internal/projects/proj-o97H2oAE/datasets/ds-UCKo4LyJ/versions/1",
        eval_dataset_name="workspaces/internal/projects/proj-o97H2oAE/datasets/ds-UCKo4LyJ/versions/1",
        train_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/ppyoloe-plus",
        train_model_display_name="std_algorithm")
    pipeline_client.compile(save_path="../../../data_annotation.yaml")
    _, run_id = pipeline_client.run(fs_name="vistudio")
