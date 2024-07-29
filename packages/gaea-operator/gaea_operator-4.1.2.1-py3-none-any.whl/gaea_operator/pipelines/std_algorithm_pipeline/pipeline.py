#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/6/27
# @Author  : wanggaofei@baidu.com, lidai@baidu.com
# @File    : pipeline.py
"""
from paddleflow.pipeline import Pipeline
from paddleflow.pipeline import CacheOptions
from paddleflow.pipeline import ContainerStep
from paddleflow.pipeline import Artifact
from paddleflow.pipeline import ExtraFS

import os
from abc import ABCMeta, abstractmethod


@Pipeline(
    name="ppyoloe_plus",
    cache_options=CacheOptions(enable=False),
)
def pipeline(accelerator: str = "T4",
             extra_fs_name: str = "vistudio",
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
             eval_dataset_name: str = "",
             transform_model_name: str = "",
             transform_model_display_name: str = "",
             ensemble_model_name: str = "",
             ensemble_model_display_name: str = "",
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

    train_params = {"train_dataset_name": train_dataset_name,
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
                    }
    train_env = {"TRAIN_DATASET_NAME": "{{train_dataset_name}}",
                 "VAL_DATASET_NAME": "{{val_dataset_name}}",
                 "MODEL_NAME": "{{model_name}}",
                 "MODEL_DISPLAY_NAME": "{{model_display_name}}",
                 "ADVANCED_PARAMETERS": "{{advanced_parameters}}",
                 "PF_EXTRA_WORK_DIR": extra_fs_mount_path,
                 "PIPELINE_ROLE": "windmill"
                 }
    train_env.update(base_env)
    train_params.update(base_params)

    script_name = "pdc_train_traffic_v13-dev8.sh"
    pdc_train_mirror = (
        "iregistry.baidu-int.com/acg_aiqp_algo/paddlecloud/ubuntu18.04:cuda11.2-cudnn8.6-gaea-std-alg-4-dev1")
    train_command = (f"cd /root/paddlejob && \
        cp $PF_WORK_DIR/pdc_train_script/std_algorithm/{script_name} . && \
        bash {script_name} {{{{train_group_name}}}} {{{{algo_id}}}} {{{{pdc_ak}}}} {{{{pdc_sk}}}} \
            {{{{k8s_gpu_cards}}}} {pdc_train_mirror} '{{{{advanced_parameters}}}}' \
              {{{{train_dataset_name}}}}")

    train = ContainerStep(name="train",
                          docker_env="iregistry.baidu-int.com/acg_aiqp_algo/paddlecloud/ubuntu18.04:cuda11.8-cudnn8.6"
                                     "-gaea-op8",
                          parameters=train_params,
                          env=train_env,
                          extra_fs=[ExtraFS(name=extra_fs_name, mount_path=extra_fs_mount_path)],
                          outputs={"output_model_uri": Artifact(), "output_uri": Artifact()},
                          command=train_command)

    return train.outputs["output_uri"]


def transform_eval_step(algorithm: str,
                        eval_step: ContainerStep = None,
                        transform_step: ContainerStep = None,
                        windmill_ak: str = "",
                        windmill_sk: str = "",
                        windmill_endpoint: str = "",
                        experiment_kind: str = "",
                        experiment_name: str = "",
                        modelstore_name: str = "",
                        tracking_uri: str = "",
                        project_name: str = "",
                        accelerator: str = "",
                        icafe_id: str = "",
                        icafe_status: str = "",
                        icafe_operator: str = ""
                        ):
    """
    Transform eval step
    """
    transform_eval_params = {"flavour": "c4m16gpu1",
                             "queue": "qtrain",
                             "windmill_ak": windmill_ak,
                             "windmill_sk": windmill_sk,
                             "windmill_endpoint": windmill_endpoint,
                             "experiment_name": experiment_name,
                             "experiment_kind": experiment_kind,
                             "tracking_uri": tracking_uri,
                             "project_name": project_name,
                             "model_store_name": modelstore_name,
                             "accelerator": accelerator,
                             "advanced_parameters": '{"conf_threshold":"0.5",'
                                                    '"iou_threshold":"0.5"}',
                             "icafe_id": icafe_id,
                             "icafe_status": icafe_status,
                             "icafe_operator": icafe_operator}

    transform_eval_env = {"PF_JOB_FLAVOUR": "{{flavour}}",
                          "PF_JOB_QUEUE_NAME": "{{queue}}",
                          "WINDMILL_AK": "{{windmill_ak}}",
                          "WINDMILL_SK": "{{windmill_sk}}",
                          "WINDMILL_ENDPOINT": "{{windmill_endpoint}}",
                          "EXPERIMENT_KIND": "{{experiment_kind}}",
                          "EXPERIMENT_NAME": "{{experiment_name}}",
                          "TRACKING_URI": "{{tracking_uri}}",
                          "PROJECT_NAME": "{{project_name}}",
                          "ACCELERATOR": "{{accelerator}}",
                          "ADVANCED_PARAMETERS": "{{advanced_parameters}}",
                          "ICAFE_ID": "{{icafe_id}}",
                          "ICAFE_OPERATOR": "{{icafe_operator}}",
                          "PIPELINE_ROLE": "windmill", }
    accelerator = get_accelerator(name=accelerator)
    transform_eval_env.update(accelerator.suggest_env())


    transform_eval = ContainerStep(name="transform-eval",
                                   docker_env="iregistry.baidu-int.com/windmill-public/inference/nvidia:v1.2.0-lidai"
                                              "-dev4",
                                   env=transform_eval_env,
                                   parameters=transform_eval_params,
                                   inputs={"input_dataset_uri": eval_step.outputs["output_dataset_uri"],
                                           "input_model_uri": transform_step.outputs["output_model_uri"]},
                                   outputs={"output_uri": Artifact()},
                                   command=f'python3 -m gaea_operator.components.transform_eval.transform_eval '
                                           f'--algorithm={algorithm} '
                                           f'--input-model-uri={{{{input_model_uri}}}} '
                                           f'--input-dataset-uri={{{{input_dataset_uri}}}} '
                                           f'--output-uri={{{{output_uri}}}} '
                                   )

    return transform_eval


class Accelerator(metaclass=ABCMeta):
    """
    Accelerator
    """
    T4 = "T4"
    V100 = "V100"
    A100 = "A100"
    R200 = "R200"

    NVIDIA = "Nvidia"
    KUNLUN = "Kunlun"

    def __init__(self, name: str = "T4"):
        self.name = name
        self.image = ""
        self.args = None
        self.env = None

    def suggest_image(self):
        """
        Suggest image
        """
        return self.image

    def suggest_env(self):
        """
        Suggest env
        """
        return self.env

    def suggest_args(self):
        """
        Suggest args
        """
        return self.args

    @abstractmethod
    def suggest_flavours(self):
        """
        Suggest flavours
        """
        raise NotImplementedError()

    @abstractmethod
    def suggest_model_server_parameters(self):
        """
        Suggest model server parameters
        """
        raise NotImplementedError()

    @abstractmethod
    def suggest_resource_tips(self):
        """
        Suggest resource tips
        """
        raise NotImplementedError()


class NvidiaAccelerator(Accelerator):
    """
    Nvidia Accelerator
    """

    def __init__(self, name: str = "T4"):
        super().__init__(name=name)
        self.image = "iregistry.baidu-int.com/windmill-public/inference/nvidia:v1.2.0-dev1"
        self.args = {"backend-config": "tensorrt,plugins=/opt/tritonserver/lib/libmmdeploy_tensorrt_ops.so"}
        self.env = \
            {
                "LD_LIBRARY_PATH":
                    "/usr/local/cuda/compat/lib:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/opt/tritonserver/lib",
                "PATH": "/opt/tritonserver/bin:/usr/local/mpi/bin:/usr/local/nvidia/bin:/usr/local/cuda/bin:"
                        "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/ucx/bin"
            }

    def suggest_flavours(self):
        """
        Suggest flavours
        """
        flavour_list = [{"name": "c8m32gpu1", "display_name": "CPU: 8核 内存: 32Gi GPU: 1卡"},
                        {"name": "c8m32gpu2", "display_name": "CPU: 8核 内存: 32Gi GPU: 2卡"},
                        {"name": "c16m64gpu2", "display_name": "CPU: 16核 内存: 64Gi GPU: 2卡"},
                        {"name": "c16m32gpu4", "display_name": "CPU: 16核 内存: 32Gi GPU: 4卡"},
                        {"name": "c16m64gpu4", "display_name": "CPU: 16核 内存: 64Gi GPU: 4卡"},
                        {"name": "c32m96gpu4", "display_name": "CPU: 32核 内存: 96Gi GPU: 4卡"}]

        return flavour_list

    def suggest_model_server_parameters(self):
        """
        Suggest model server parameters
        """
        resource = {"accelerator": self.name,
                    "gpu": "75",
                    "limits": {"cpu": "10", "mem": "10Gi"},
                    "requests": {"cpu": "100m", "mem": "50Mi"}}
        model_server_parameters = {
            "image": self.image,
            "env": self.env,
            "args": self.args,
            "resource": resource}

        return model_server_parameters

    def suggest_resource_tips(self):
        """
        Suggest resource tips
        """
        return ["config.maxResources.scalarResources.nvidia.com/gpu>1"]


class KunlunAccelerator(Accelerator):
    """
    Kunlun Accelerator
    """

    def __init__(self, name: str = "R200"):
        super().__init__(name=name)
        self.image = "iregistry.baidu-int.com/windmill-public/inference/kunlun:v1.2.0"
        self.args = {"backend-config": "tensorrt,plugins=/opt/tritonserver/lib/libmmdeploy_tensorrt_ops.so"}
        self.env = \
            {
                "LD_LIBRARY_PATH":
                    "/opt/tritonserver/backends/paddlelite:/opt/tritonserver/backends/Kunlun:$LD_LIBRARY_PATH",
                "XTCL_L3_SIZE": "16776192"
            }

    def suggest_flavours(self):
        """
        Suggest flavours
        """
        flavour_list = [{"name": "c4m16xpu1", "display_name": "CPU: 4核 内存: 16Gi XPU: 1卡"}]
        return flavour_list

    def suggest_model_server_parameters(self):
        """
        Suggest model server parameters
        """

        resource = {"accelerator": self.name,
                    "gpu": "7500",
                    "limits": {"cpu": "10", "mem": "10Gi"},
                    "requests": {"cpu": "100m", "mem": "50Mi"}}
        model_server_parameters = {
            "image": self.image,
            "env": self.env,
            "backend": self.args,
            "resource": resource}

        return model_server_parameters

    def suggest_resource_tips(self):
        """
        Suggest resource tips
        """
        return ["config.maxResources.scalarResources.baidu.com/xpu-mem>1"]


def get_accelerator(name: str = None, kind: str = None) -> Accelerator:
    """
    Get accelerator.
    """
    if kind == Accelerator.NVIDIA:
        return NvidiaAccelerator(name=name)
    if kind == Accelerator.KUNLUN:
        return KunlunAccelerator(name=name)

    if name in (Accelerator.T4, Accelerator.V100, Accelerator.A100):
        return NvidiaAccelerator(name=name)
    elif name in (Accelerator.R200,):
        return KunlunAccelerator(name=name)
    else:
        raise Exception("Unsupported accelerator: {}".format(name))


def inference_step(eval_step: ContainerStep = None,
                   package_step: ContainerStep = None,
                   windmill_ak: str = "",
                   windmill_sk: str = "",
                   windmill_endpoint: str = "",
                   experiment_kind: str = "",
                   experiment_name: str = "",
                   model_store_name: str = "",
                   tracking_uri: str = "",
                   project_name: str = "",
                   accelerator: str = "",
                   icafe_id: str = "",
                   icafe_operator: str = ""
                   ):
    """
    Inference step
    """
    inference_params = {"flavour": "c4m16gpu1",
                        "queue": "qtrain",
                        "windmill_ak": windmill_ak,
                        "windmill_sk": windmill_sk,
                        "windmill_endpoint": windmill_endpoint,
                        "experiment_name": experiment_name,
                        "experiment_kind": experiment_kind,
                        "tracking_uri": tracking_uri,
                        "project_name": project_name,
                        "model_store_name": model_store_name,
                        "accelerator": accelerator,
                        "advanced_parameters": '{"conf_threshold":"0.5"}',
                        "icafe_id": icafe_id,
                        "icafe_operator": icafe_operator}
    inference_env = {"PF_JOB_FLAVOUR": "{{flavour}}",
                     "PF_JOB_QUEUE_NAME": "{{queue}}",
                     "WINDMILL_AK": "{{windmill_ak}}",
                     "WINDMILL_SK": "{{windmill_sk}}",
                     "WINDMILL_ENDPOINT": "{{windmill_endpoint}}",
                     "EXPERIMENT_KIND": "{{experiment_kind}}",
                     "EXPERIMENT_NAME": "{{experiment_name}}",
                     "TRACKING_URI": "{{tracking_uri}}",
                     "PROJECT_NAME": "{{project_name}}",
                     "ACCELERATOR": "{{accelerator}}",
                     "ICAFE_ID": "{{icafe_id}}",
                     "ICAFE_OPERATOR": "{{icafe_operator}}",
                     "ADVANCED_PARAMETERS": "{{advanced_parameters}}",
                     "PIPELINE_ROLE": "windmill",
                     }
    accelerator = get_accelerator(name=accelerator)
    inference_env.update(accelerator.suggest_env())

    inference = ContainerStep(name="inference",
                              docker_env="iregistry.baidu-int.com/windmill-public/inference/nvidia:v1.2.0-lidai-dev4",
                              env=inference_env,
                              parameters=inference_params,
                              inputs={"input_dataset_uri": eval_step.outputs["output_dataset_uri"],
                                      "input_model_uri": package_step.outputs["output_model_uri"]},
                              outputs={"output_uri": Artifact()},
                              command=f'python3 -m gaea_operator.components.inference.inference '
                                      f'--input-model-uri={{{{input_model_uri}}}} '
                                      f'--input-dataset-uri={{{{input_dataset_uri}}}} '
                                      f'--output-uri={{{{output_uri}}}}  '
                              )

    return inference


def package_step(algorithm: str,
                 transform_eval_step: ContainerStep = None,
                 transform_step: ContainerStep = None,
                 windmill_ak: str = "",
                 windmill_sk: str = "",
                 windmill_endpoint: str = "",
                 experiment_kind: str = "",
                 experiment_name: str = "",
                 modelstore_name: str = "",
                 tracking_uri: str = "",
                 project_name: str = "",
                 accelerator: str = "",
                 ensemble_model_name: str = "",
                 ensemble_model_display_name: str = "",
                 sub_model_names: str = "",
                 scene: str = "",
                 icafe_id: str = "",
                 icafe_operator: str = ""
                 ):
    """
    Package step
    """
    package_params = {"flavour": "c4m16",
                      "queue": "qtrain",
                      "windmill_ak": windmill_ak,
                      "windmill_sk": windmill_sk,
                      "windmill_endpoint": windmill_endpoint,
                      "experiment_name": experiment_name,
                      "experiment_kind": experiment_kind,
                      "tracking_uri": tracking_uri,
                      "project_name": project_name,
                      "model_store_name": modelstore_name,
                      "accelerator": accelerator,
                      "ensemble_model_name": ensemble_model_name,
                      "ensemble_model_display_name": ensemble_model_display_name,
                      "sub_model_names": sub_model_names,
                      "scene": scene,
                      "icafe_id": icafe_id,
                      "icafe_operator": icafe_operator}
    package_env = {"PF_JOB_FLAVOUR": "{{flavour}}",
                   "PF_JOB_QUEUE_NAME": "{{queue}}",
                   "WINDMILL_AK": "{{windmill_ak}}",
                   "WINDMILL_SK": "{{windmill_sk}}",
                   "WINDMILL_ENDPOINT": "{{windmill_endpoint}}",
                   "EXPERIMENT_KIND": "{{experiment_kind}}",
                   "EXPERIMENT_NAME": "{{experiment_name}}",
                   "TRACKING_URI": "{{tracking_uri}}",
                   "PROJECT_NAME": "{{project_name}}",
                   "ACCELERATOR": "{{accelerator}}",
                   "ENSEMBLE_MODEL_NAME": "{{ensemble_model_name}}",
                   "ENSEMBLE_MODEL_DISPLAY_NAME": "{{ensemble_model_display_name}}",
                   "SUB_MODEL_NAMES": "{{sub_model_names}}",
                   "SCENE": "{{scene}}",
                   "ICAFE_ID": "{{icafe_id}}",
                   "ICAFE_OPERATOR": "{{icafe_operator}}",
                   "PIPELINE_ROLE": "windmill",
                   }

    # TODO：update gaea-operator 镜像
    package = ContainerStep(name="package",
                            docker_env="iregistry.baidu-int.com/windmill-public/inference/nvidia:v1.2.0-lidai-dev4",
                            env=package_env,
                            parameters=package_params,
                            inputs={"input_model_uri": transform_step.outputs["output_model_uri"]},
                            outputs={"output_model_uri": Artifact(), "output_uri": Artifact()},
                            command=f'python3 -m gaea_operator.components.package.package '
                                    f'--algorithm={algorithm} '
                                    f'--input-model-uri={{{{input_model_uri}}}} '
                                    f'--output-uri={{{{output_uri}}}} '
                                    f'--output-model-uri={{{{output_model_uri}}}} '
                            ).after(transform_eval_step)

    return package


if __name__ == "__main__":
    pipeline_client = pipeline(
        accelerator="T4",
        windmill_ak="a1a9069e2b154b2aa1a83ed12316d163",
        windmill_sk="eefac23d2660404e93855197ce60efb3",
        windmill_endpoint="http://10.27.240.5:8340",
        experiment_kind="Aim",
        experiment_name="ppyoloe_plus_m",
        tracking_uri="aim://10.27.240.5:8329",
        project_name="workspaces/internal/projects/proj-o97H2oAE",
        train_dataset_name="workspaces/internal/projects/proj-o97H2oAE/datasets/ds-UCKo4LyJ/versions/1",
        val_dataset_name="workspaces/internal/projects/proj-o97H2oAE/datasets/ds-UCKo4LyJ/versions/1",
        eval_dataset_name="workspaces/internal/projects/proj-o97H2oAE/datasets/ds-UCKo4LyJ/versions/1",
        train_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/ppyoloe-plus",
        train_model_display_name="ppyoloe-plus",
        transform_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/ppyoloe-plus-t4",
        transform_model_display_name="ppyoloe-plus-t4",
        ensemble_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/ppyoloe-plus-ensemble",
        ensemble_model_display_name="ppyoloe-plus-ensemble")
    pipeline_client.compile(save_path="./pipeline.yaml")
    #_, run_id = pipeline_client.run(fs_name="vistudio")
