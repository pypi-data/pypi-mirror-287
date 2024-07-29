#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/06/05
# @Author  : 李岱
# @File    : pipeline.py
"""
from typing import List

from paddleflow.pipeline import Pipeline
from paddleflow.pipeline import CacheOptions
from paddleflow.pipeline import ContainerStep
from paddleflow.pipeline import Artifact
from paddleflow.pipeline import ExtraFS

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
             model_store_name: str = "",
             tracking_uri: str = "",
             project_name: str = "",
             input_dataset_name: List[str] = None,
             output_dataset_name: str = "",
             model_name: str = "",
             model_artifact_version: str = "",
             pipeline_category: str = "",
             workspace_id: str = "",
             icafe_id: str = "",
             icafe_operator: str = "",
             label_confidence_threshold: str = "",
             mining_key_word: str = "",
             mining_key_word_description: str = "",
             mining_algorithm: str = "",
             ):
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
                   "model_store_name": model_store_name,
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

    datamining_params = {"input_dataset_name": input_dataset_name,
                         "output_dataset_name": output_dataset_name,
                         "label_confidence_threshold": label_confidence_threshold,
                         "model_store_name": model_store_name,
                         "model_name": model_name,
                         "model_artifact_version": model_artifact_version,
                         "pipeline_category": pipeline_category,
                         "mining_key_word": mining_key_word,
                         "mining_key_word_description": mining_key_word_description,
                         "mining_algorithm": mining_algorithm,
                         }
    datamining_env = {"INPUT_DATASET_NAME": "{{input_dataset_name}}",
                      "OUTPUT_DATASET_NAME": "{{output_dataset_name}}",
                      "LABEL_CONFIDENCE_THRESHOLD": "{{label_confidence_threshold}}",
                      "MODEL_STORE_NAME": "{{model_store_name}}",
                      "MODEL_NAME": "{{model_name}}",
                      "MODEL_ARTIFACT_VERSION": "{{model_artifact_version}}",
                      "PF_EXTRA_WORK_DIR": extra_fs_mount_path,
                      "PIPELINE_ROLE": "windmill",
                      "PIPELINE_CATEGORY": "{{pipeline_category}}",
                      "MINING_KEY_WORD": "{{mining_key_word}}",
                      "MINING_KEY_WORD_DESCRIPTION": "{{mining_key_word_description}}",
                      "MINING_ALGORITHM": "{{mining_algorithm}}",
                      }
    datamining_env.update(base_env)
    datamining_params.update(base_params)

    data_mining = ContainerStep(name="datamining",
                                docker_env="iregistry.baidu-int.com/acg_aiqp_algo/cv-dev/ivl:v0.1.1",
                                parameters=datamining_params,
                                env=datamining_env,
                                extra_fs=[ExtraFS(name=extra_fs_name, mount_path=extra_fs_mount_path)],
                                outputs={"output_model_uri": Artifact(), "output_uri": Artifact()},
                                command=f'cd /root && '
                                        f'export LD_LIBRARY_PATH=/opt/conda/envs/data/opt/conda/envs/data/lib'
                                        f':$LD_LIBRARY_PATH &&'
                                        f'export PYTHONPATH=$PYTHONPATH:/opt/conda/envs/data/opt/conda/envs/data/lib'
                                        f'/python311.zip:/opt/conda/envs/data/opt/conda/envs/data/lib/python3.11:/opt'
                                        f'/conda/envs/data/opt/conda/envs/data/lib/python3.11/lib-dynload:/opt/conda'
                                        f'/envs/data/opt/conda/envs/data/lib/python3.11/site-packages:/usr/local/lib'
                                        f'/python3.8/dist-package &&'
                                        f'/opt/conda/envs/data/opt/conda/envs/data/bin/python3 -m '
                                        f'gaea_operator.components.data_mining.data_mining '
                                        f'--output-model-uri={{{{output_model_uri}}}} '
                                        f'--output-uri={{{{output_uri}}}} '
                                )

    return data_mining.outputs["output_uri"]


if __name__ == "__main__":
    pipeline_client = pipeline(
        windmill_ak="a1a9069e2b154b2aa1a83ed12316d163",
        windmill_sk="eefac23d2660404e93855197ce60efb3",
        windmill_endpoint="http://10.27.240.5:8340",
        experiment_kind="Aim",
        experiment_name="std_algorithm",
        tracking_uri="aim://10.27.240.5:8329",
        project_name="workspaces/internal/projects/proj-o97H2oAE",
        input_dataset_name=["workspaces/internal/projects/proj-o97H2oAE/datasets/ds-UCKo4LyJ/versions/1"],
        output_dataset_name="workspaces/internal/projects/proj-o97H2oAE/datasets/ds-UCKo4LyJ/versions/1",
        )
    pipeline_client.compile(save_path="./pipeline.yaml")
    #_, run_id = pipeline_client.run(fs_name="vistudio")
