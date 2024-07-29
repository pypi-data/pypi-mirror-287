# -*- coding: utf-8 -*-
"""
Copyright(C) 2023 baidu, Inc. All Rights Reserved

# @Time : 2024/3/8 15:04
# @Author : yangtingyu01
# @Email: yangtingyu01@baidu.com
# @File : pipeline.py
# @Software: PyCharm
"""
import pdb

from vistudiost.components import render_st_dataset, render_st_model, render_st_model_store, \
    render_st_endpoint_hub, render_st_compute, render_st_flavour, \
    render_st_deploy, render_st_create_job, render_st_package, \
    render_st_popup, render_st_model_detail
from vistudiost.components.create_job_component import CreateJobComponent
# 使用 v1 版本的 get_spec_raw
from vistudiost.pages.pipeline.base import get_spec_raw, \
    eval_part, transform_eval_part, inference_part
from vistudiost.components.advanced_parameter_component import get_advance_parameters
from windmillcomputev1.client.compute_api_compute import parse_compute_name
from windmillmodelv1.client.model_api_model import parse_model_name
from windmilltrainingv1.client.training_api_project import ProjectName
from vistudiost.pages.pipeline.base import set_pipeline_params
from vistudiost.utils.render import st_write, object_format, artifact_version_format, compute_format, find_index
from gaea_operator.utils.accelerator import get_accelerator
from vistudiost.cache.cache import get_project, get_pipeline, get_artifact, get_workspace_id, list_project
import bcelogger as logger
import streamlit as st
import re
from vistudiost.components.advanced_parameter_component import render



def basic_part(config):
    """
    基础信息
    Returns:

    """
    basic_ok = True
    st_write("基础信息", font_size=16)
    st.markdown("")
    basic_param = {}
    pipeline_resp = get_pipeline(st.session_state.windmill["client"],
                                 request={"workspace_id": config["workspace_id"],
                                          "project_name": config["project_name"],
                                          "pipeline_name": config["pipeline_name"]})
    if config["workspace_id"] == "public":
        workspace_id = get_workspace_id(st.session_state.windmill["client"])
        project_list = list_project(st.session_state.windmill["client"],
                                    {"workspace_id": workspace_id})
        project_name = st.selectbox("项目名称",
                                    project_list,
                                    format_func=object_format,
                                    index=find_index(project_list, "localName",
                                                     getattr(st.session_state.config.get("job_name", {}),
                                                             "project_name",
                                                             "")),
                                    key="user_project_name")
        project_name = project_name.get("localName")
        if not project_name:
            basic_ok = False
            st.error("没有项目可选")
    else:
        workspace_id = config["workspace_id"]
        response = get_project(st.session_state.windmill["client"],
                               request={"workspace_id": workspace_id,
                                        "project_name": config["project_name"]})
        basic_param["project_name"] = getattr(response, "name", "")
        st.text_input("项目名称", object_format(response),
                      key="user_project_name", disabled=True)
        project_name = config["project_name"]
    model_store_name, ok_model_store = render_st_model_store(["模型仓库选择"],
                                                             request={
                                                                 "workspace_id": workspace_id},
                                                             pipeline_param_keys={
                                                                 "model_store_name": "model_store_name"},
                                                             pipeline_params=config["parameters"],
                                                             permission=config["permission"])
    basic_param.update(model_store_name)
    # pipeline_resp = get_pipeline(st.session_state.windmill["client"], config)
    basic_param["pipeline_category"] = getattr(pipeline_resp, "category", {}).get("category", "")
    basic_param["pipeline_display_name"] = getattr(pipeline_resp, "displayName", "")
    basic_param["workspace_id"] = workspace_id
    basic_param["project_name"] = project_name
    return basic_param, ok_model_store and basic_ok


def train_part(config,
               workspace_id,
               project_name,
               model_store_name,
               pipeline_display_name,
               pipeline_category,
               train_advance_parameters):
    """
    模型训练
    Args:
        config:
        train_advance_parameters:
        model_store_name
        pipeline_category
        pipeline_display_name

    Returns:

    """
    st.markdown("")
    st_write("模型训练", font_size=16)
    st.markdown("")

    train_parameters = {}

    train_dataset, ok_train_dataset = render_st_dataset(["训练集选择"],
                                                        request={
                                                            "workspace_id": workspace_id,
                                                            "project_name": project_name
                                                        },
                                                        pipeline_param_keys={
                                                            "dataset_name": "train.train_dataset_name"},
                                                        pipeline_params=config["parameters"],
                                                        permission=config["permission"])
    train_parameters.update(train_dataset)

    val_dataset, ok_eval_dataset = render_st_dataset(["验证集选择"],
                                                     request={
                                                         "workspace_id": workspace_id,
                                                         "project_name": project_name
                                                     },
                                                     pipeline_param_keys={
                                                         "dataset_name": "train.val_dataset_name"},
                                                     pipeline_params=config["parameters"],
                                                     permission=config["permission"])
    if val_dataset["train.val_dataset_name"] == train_parameters["train.train_dataset_name"]:
        st_write("训练集的数据建议不要出现在验证集中，否则会导致评估指标产生极大的偏差")
    train_parameters.update(val_dataset)

    compute_name, ok_compute = render_st_compute(["计算资源"],
                                                 request={
                                                     "workspace_id": workspace_id,
                                                     "project_name": project_name,
                                                     "tips": ["config.maxResources.scalarResources.nvidia.com/gpu>1",
                                                              f"tags.usage=train",
                                                              "training"]},
                                                 pipeline_param_keys={"compute_name": "train.compute_name"},
                                                 pipeline_params=config["parameters"],
                                                 permission=config["permission"],
                                                 )
    train_parameters.update(compute_name)
    flavour_list = [{"name": "c16m32", "display_name": "CPU: 16核 内存: 32Gi 无GPU"}]

    flavour_name, ok_flavour = render_st_flavour(["资源套餐"],
                                                 request={"name": "gpu", "flavour_list": flavour_list},
                                                 pipeline_param_keys={"flavour_name": "train.flavour"},
                                                 pipeline_params=config["parameters"],
                                                 permission=config["permission"])
    train_parameters.update(flavour_name)
    model, ok_model = render_st_model(["模型发布", "模型选择"],
                                      pipeline_param_keys={"model_name": "train.model_name",
                                                           "model_display_name": "train.model_display_name"},
                                      pipeline_params=config["parameters"],
                                      request={
                                          "model_store_name": model_store_name,
                                          "workspace_id": workspace_id,
                                          "model_display_name": pipeline_display_name + '-模型',
                                          "categories": [pipeline_category]},
                                      permission=config["permission"])
    train_parameters.update(model)

    train_config_params_uri = ""
    if_train_config_params_uri_disabled = False
    ok_v2x_train_config = True

    if config["parameters"].get("train_config_params_uri"):
        train_config_params_uri = config["parameters"].get("train_config_params_uri")
        if_train_config_params_uri_disabled = True
    train_config_params_uri_input = st.text_input("训练配置文件", train_config_params_uri,
                                                  key=f"train_config_params_uri", max_chars=120,
                                                  disabled=if_train_config_params_uri_disabled)
    st.info("文件位置固定前缀为 bos:/wsmp/store/train_cfg/std_algorithm/ ，文件格式为 tar，文本框里填写相对目录（例如 test/train_config.tar）, "
            "其中必须包含训练配置文件 input_config.yaml。目前仅支持标准化后的配置文件，配置文件中 num_classes 和 CUDA_VISIBLE_DEVICES 配置请在上传前进行设置")
    if not train_config_params_uri_input:
        st.error("请输入配置文件名称")
        ok_v2x_train_config = False

    train_params_config = {}
    train_params_config['train_config_params_uri'] = train_config_params_uri_input
    train_parameters.update(train_params_config)

    advance_param, advance_param_ok = render_st_advanced_parameters("train", train_advance_parameters)
    train_parameters.update(advance_param)

    is_ok = ok_train_dataset and ok_eval_dataset and ok_compute and ok_flavour and ok_model and ok_v2x_train_config
    return train_parameters, is_ok


def eval_part(workspace_id,
              project_name,
              compute_name,
              pipeline_category):
    """
    模型评估
    Args:

    Returns:

    """
    st_write("模型评估", font_size=16)
    eval_param = {}
    dataset, ok_dataset = render_st_dataset(["测试集选择"],
                                            request={"workspace_id": workspace_id,
                                                     "project_name": project_name
                                                     },
                                            pipeline_param_keys={"dataset_name": "eval.dataset_name"},
                                            pipeline_params=st.session_state.config["parameters"],
                                            permission=st.session_state.config["permission"])
    eval_param.update(dataset)
    st.text_input("计算资源", value=parse_compute_name(compute_name).local_name if parse_compute_name(
        compute_name) is not None else "",
                  key='eval.compute_name', disabled=True)

    eval_param["eval.compute_name"] = compute_name

    return eval_param, ok_dataset


def transform_part(config,
                   workspace_id,
                   project_name,
                   model_store_name,
                   model_name,
                   pipeline_display_name,
                   transform_advance_parameters,
                   train_advance_parameters):
    """
    模型转换
    Args:
        config:
        train_advance_parameters:
        transform_advance_parameters:
        pipeline_display_name:
        model_name
        model_store_name
    Returns:

    """
    st.markdown("")
    st_write("模型转换", font_size=16)
    st.markdown("")
    param_trans = {}
    model_name_resp = parse_model_name(model_name)
    if model_name_resp is not None:
        model_name = model_name_resp.local_name
    accelerator = st.selectbox("目标显卡类型",
                               options=[config["parameters"]["transform.accelerator"]]
                               if config.get("parameters", {})
                               else ["A10"],
                               key="transform.accelerator")
    accelerator = get_accelerator(accelerator)
    flavour_name = accelerator.suggest_flavours()[0]["name"]
    compute_name, ok_compute = render_st_compute(["计算资源"],
                                                 request={
                                                     "workspace_id": workspace_id,
                                                     "project_name": project_name,
                                                     "tips": [accelerator.suggest_resource_tips()[0],
                                                              "training",
                                                              f"tags.accelerator={accelerator.name}"]},
                                                 pipeline_param_keys={
                                                     "compute_name": "transform.compute_name"},
                                                 pipeline_params=config["parameters"],
                                                 permission=config["permission"]
                                                 )
    if parse_model_name(model_name) is not None:
        model_name = parse_model_name(model_name).local_name
    model_display_name = st.text_input("目标模型", f'{pipeline_display_name}'
                                                   f'-{accelerator.name}',
                                       key=f"transform.transform_model_display_name", max_chars=80, disabled=True)
    param_trans["transform.transform_model_display_name"] = model_display_name
    model_name = st.text_input(":red[*]目标模型系统名称",
                               f"{model_name}-{accelerator.name}" if model_name else f"-{accelerator.name}",
                               key="transform.transform_model_name", max_chars=36, disabled=True)
    param_trans["transform.transform_model_name"] = model_store_name + "/models/" + model_name
    advance_param, advance_param_ok = render_st_advanced_parameters("transform",
                                                  transform_advance_parameters,
                                                  train_advance_parameters)

    param_trans["transform.accelerator"] = accelerator.name
    param_trans["transform.flavour"] = flavour_name
    param_trans.update(advance_param)
    param_trans.update(compute_name)

    return param_trans, ok_compute


def package_part(config,
                 workspace_id,
                 model_store_name,
                 model_name,
                 model_display_name,
                 accelerator,
                 compute_name):
    """
    模型包组装
    Returns:

    """
    st.markdown("")
    st_write("模型组装", font_size=16)
    st.markdown("")

    if model_name is not None and parse_model_name(model_name) is not None:
        model_name = parse_model_name(model_name).local_name

    model, ok_model = render_st_model(["目标模型包", "模型包选择"],
                                      pipeline_param_keys={
                                          "model_name": "package.ensemble_model_name",
                                          "model_display_name": "package.ensemble_model_display_name"},
                                      pipeline_params=config["parameters"],
                                      request={
                                          "model_store_name": model_store_name,
                                          "model_display_name": f"{model_display_name}-模型包",
                                          "model_name": f"{model_name}-ensemble"
                                          if model_name else f"-ensemble",
                                          "workspace_id": workspace_id,
                                          "categories": ["Image/Ensemble"]},
                                      permission=config["permission"])
    model.update({"package.compute_name": compute_name,
                  "package.accelerator": accelerator})
    return model, ok_model


def icafe_part(config):
    """
    icafe 卡片信息同步
    Args:
        None
    Returns:
        Dict
    """
    st.markdown("")
    st_write("iCafe 信息", font_size=16)
    st.markdown("")

    config_paramerters = config['parameters']
    icafe_parameters = {}
    is_icafe_ok = True

    if_icafe_id_disabled = False
    icafe_id = ""
    if config_paramerters.get("icafe_id"):
        icafe_id = config_paramerters.get("icafe_id")
        if_icafe_id_disabled = True

    icafe_id = st.text_input("[必填]卡片 ID", icafe_id, key=f"icafe_id", max_chars=80, disabled=if_icafe_id_disabled)
    if not validate_icafe_id_input(icafe_id):
        is_icafe_ok = False
        st.error("请输入正确的卡片 ID，支持仅输入卡片数字编号（如 477 ）或完整卡片名称（如 cv-algorithm-477 ）")

    icafe_parameters["icafe_id"] = icafe_id

    if_icafe_operator_disabled = False
    icafe_operator = ""
    if config_paramerters.get("icafe_operator"):
        icafe_operator = config_paramerters.get("icafe_operator")
        if_icafe_operator_disabled = True

    icafe_operator_input = st.text_input("[必填]操作人（邮箱前缀）", icafe_operator,
                                         key=f"icafe_opeartor", max_chars=80, disabled=if_icafe_operator_disabled)
    if icafe_operator_input:
        validate_operator_result = validate_icafe_operator_input(icafe_operator_input)
        if validate_operator_result:
            icafe_parameters["icafe_operator"] = icafe_operator_input
        else:
            icafe_parameters["icafe_operator"] = ""
            is_icafe_ok = False
            st.error("请输入正确的操作人（邮箱前缀）")

    return icafe_parameters, is_icafe_ok


def validate_icafe_id_input(icafe_id_input):
    number_pattern = r'^\d+$'
    cv_pattern = r'^cv-algorithm-(\d+)$'

    # 判断并提取数字
    if re.match(number_pattern, icafe_id_input):
        return int(icafe_id_input)
    elif match := re.match(cv_pattern, icafe_id_input):
        return int(match.group(1))
    else:
        return None


def validate_icafe_operator_input(icafe_operator_input):
    pattern = r'^[a-zA-Z0-9]+([._-]?[a-zA-Z0-9]+)*$'

    # 使用正则表达式进行匹配
    if re.match(pattern, icafe_operator_input):
        return True
    else:
        return None


def paddlecloud_part(config):
    """
    pdc 提交任务
    Args:
        None
    Returns:
        Dict
    """
    st.markdown("")
    st_write("PaddleCloud作业提交信息", font_size=16)
    st.markdown("")

    config_paramerters = config['parameters']
    pdc_parameters = {}

    if_pdc_ak_disabled = False
    pdc_ak = ""
    if config_paramerters.get("pdc_ak"):
        pdc_ak = config_paramerters.get("pdc_ak")
        if_pdc_ak_disabled = True
    pdc_ak = st.text_input("[必填]paddlecloud 提交任务 个人AK", value=pdc_ak, max_chars=80, disabled=if_pdc_ak_disabled)

    if_pdc_sk_disabled = False
    pdc_sk = ""
    if config_paramerters.get("pdc_ak"):
        pdc_sk = config_paramerters.get("pdc_sk")
        if_pdc_sk_disabled = True
    pdc_sk = st.text_input("[必填]paddlecloud 提交任务 个人SK", value=pdc_sk, max_chars=80, disabled=if_pdc_sk_disabled)

    if_algo_id_disabled = False
    algo_id = ""
    if config_paramerters.get("algo_id"):
        algo_id = config_paramerters.get("algo_id")
        if_algo_id_disabled = True
    algo_id = st.text_input("[必填]算法ID，需由个人创建，并确认与AK/SK绑定", value=algo_id, max_chars=80,
                            disabled=if_algo_id_disabled)

    # train_group_name = st.text_input("训练资源Group", value="itd2-16g-0-yq01-k8s-gpu-v100-8", max_chars=80)
    if_train_group_name_disabled = False
    train_group_name = ""
    if config_paramerters.get("train_group_name"):
        train_group_name = config_paramerters.get("train_group_name")
        if_train_group_name_disabled = True
    train_group_name = st.text_input("[必填]训练资源Group", value=train_group_name, max_chars=80,
                                     disabled=if_train_group_name_disabled)

    if_k8s_gpu_cards_disabled = False
    k8s_gpu_cards = 4
    if config_paramerters.get("k8s_gpu_cards"):
        k8s_gpu_cards = config_paramerters.get("k8s_gpu_cards")
        if_k8s_gpu_cards_disabled = True
    k8s_gpu_cards = st.text_input("[必填]PDC任务占用卡数，注意是否为可选择卡数，否则可能会导致提交任务失败",
                                  value=k8s_gpu_cards, disabled=if_k8s_gpu_cards_disabled)

    is_pdc_train_mirror_disabled = False
    # Docker file
    # last Base: FROM iregistry.baidu-int.com/acg_aiqp_algo/paddlecloud/ubuntu18.04-cuda11.2-cudnn8:cuda11.2-cudnn8.6-gaea-traffic-v3
    # FROM iregistry.baidu-int.com/acg_aiqp_algo/paddlecloud/ubuntu18.04:cuda11.2-cudnn8.6-gaea-std-alg-2
    #
    # # v2x commit 5da1ef6018f00a18c5b97325e4c43551ed9f4a50
    # RUN rm -rf /root/train_code/v2x_model_standardization && \
    #   mkdir -p /root/train_code && \
    #   cd /root && \
    #   wget https://bj.bcebos.com/v1/wsmp/store/cv/lidai/v2x-model/v2x-model-standardization.tar?authorization=bce-auth-v1%2FALTAKpFzlFVB6cKIXJuubsqzK5%2F2024-05-31T03%3A05%3A01Z%2F-1%2Fhost%2F51a80e61c1ddd009fdca78c28bac5e03a3ed9b51c3844ed0a7d19c2db51db259 -O v2x-model-standardization.tar && \
    #   tar -xf v2x-model-standardization.tar && \
    #   mv v2x-model-standardization/* train_code
    #
    # COPY mount.sh /root/paddlejob/
    # WORKDIR /root/paddlejob
    pdc_train_mirror = (
        "iregistry.baidu-int.com/acg_aiqp_algo/paddlecloud/ubuntu18.04:"
        "cuda11.2-cudnn8.6-gaea-std-alg-3-export_model-fix_dataprocess_too_long-liubo41")
    if config_paramerters.get("pdc_train_mirror"):
        pdc_train_mirror = config_paramerters.get("pdc_train_mirror")
        is_pdc_train_mirror_disabled = True
    pdc_train_mirror = st.text_input("[必填]PDC任务训练镜像",
                                     value=pdc_train_mirror, disabled=is_pdc_train_mirror_disabled)

    pdc_parameters["pdc_ak"] = pdc_ak
    pdc_parameters["pdc_sk"] = pdc_sk
    pdc_parameters["algo_id"] = algo_id
    pdc_parameters["train_group_name"] = train_group_name
    pdc_parameters["k8s_gpu_cards"] = k8s_gpu_cards
    pdc_parameters["pdc_train_mirror"] = pdc_train_mirror
    pdc_ok = True
    if pdc_ak == "" or pdc_sk == "" or algo_id == "" or train_group_name == "" or k8s_gpu_cards == "":
        pdc_ok = False

    return pdc_parameters, pdc_ok


def get_parts(config, basic_parameter):
    """
    get_parts
    Args:
        config:
        basic_parameter:

    Returns:

    """
    train_advance_parameters = get_advance_parameters("train_parameter.yaml")
    if train_advance_parameters is None:
        return
    transform_advance_parameters = get_advance_parameters("transform_parameter.yaml")
    train_parameter, train_ok = train_part(config,
                                           basic_parameter["workspace_id"],
                                           basic_parameter["project_name"],
                                           basic_parameter["model_store_name"],
                                           basic_parameter["pipeline_display_name"],
                                           basic_parameter["pipeline_category"],
                                           train_advance_parameters)
    eval_parameter, eval_ok = eval_part(basic_parameter["workspace_id"],
                                        basic_parameter["project_name"],
                                        train_parameter["train.compute_name"],
                                        basic_parameter["pipeline_category"])
    trans_parameter, trans_ok = transform_part(config,
                                               basic_parameter["workspace_id"],
                                               basic_parameter["project_name"],
                                               basic_parameter["model_store_name"],
                                               train_parameter["train.model_name"],
                                               train_parameter["train.model_display_name"],
                                               transform_advance_parameters,
                                               train_advance_parameters
                                               )
    trans_eval_parameter = transform_eval_part(eval_parameter["eval.dataset_name"],
                                               trans_parameter["transform.compute_name"],
                                               trans_parameter["transform.flavour"],
                                               trans_parameter["transform.accelerator"])
    package_parameter, package_ok = package_part(config,
                                                 basic_parameter["workspace_id"],
                                                 basic_parameter["model_store_name"],
                                                 trans_parameter["transform.transform_model_name"],
                                                 trans_parameter["transform.transform_model_display_name"],
                                                 trans_parameter["transform.accelerator"],
                                                 trans_parameter["transform.compute_name"])
    inference_parameter = inference_part(trans_parameter["transform.compute_name"],
                                         package_parameter["package.ensemble_model_name"],
                                         trans_parameter["transform.flavour"],
                                         get_accelerator(trans_parameter["transform.accelerator"]))
    return train_parameter, train_ok, \
        eval_parameter, eval_ok, \
        trans_parameter, trans_ok, \
        trans_eval_parameter, \
        package_parameter, package_ok, \
        inference_parameter


def main():
    """
    Args:
    Returns:

    """
    config = st.session_state.config
    set_pipeline_params()

    basic_parameter, basic_ok = basic_part(config)

    train_parameter, train_ok, \
        eval_parameter, eval_ok, \
        trans_parameter, trans_ok, \
        trans_eval_parameter, \
        package_parameter, package_ok, \
        inference_parameter = get_parts(config, basic_parameter)

    icafe_parameters, icafe_ok = icafe_part(config)
    pdc_parameters, pdc_ok = paddlecloud_part(config)

    parameters = {}
    parameters.update(train_parameter)
    parameters.update(eval_parameter)
    parameters.update(trans_parameter)
    parameters.update(trans_eval_parameter)
    parameters.update(package_parameter)
    parameters.update(inference_parameter)
    parameters.update(icafe_parameters)
    parameters.update(pdc_parameters)

    parameters["windmill_ak"] = st.session_state.windmill["client"].config.credentials.access_key_id.decode('utf-8')
    parameters["windmill_sk"] = st.session_state.windmill["client"].config.credentials.secret_access_key.decode('utf-8')
    parameters["windmill_endpoint"] = st.secrets.windmill.endpoint
    project_name = ProjectName(workspace_id=basic_parameter["workspace_id"], local_name=basic_parameter["project_name"])
    parameters["project_name"] = project_name.get_name()
    parameters["model_store_name"] = basic_parameter["model_store_name"]

    artifact_resp = get_artifact(st.session_state.windmill["client"], st.session_state.config["artifact_name"])
    if getattr(artifact_resp, "tags") and artifact_resp.tags.get("scene"):
        parameters["scene"] = artifact_resp.tags.get("scene")
    # todo 当使用 paddle cloud 时，需要填写相关信息，此为可选项
    is_ok = basic_ok and train_ok and eval_ok and package_ok and trans_ok and icafe_ok

    if config["permission"] == "readwrite":
        spec_raw = get_spec_raw(trans_parameter["transform.accelerator"])
        request = {"parameters": parameters,
                   "version": config["version"],
                   "object_name": config["object_name"],
                   "pipeline": config["pipeline_name"],
                   "workspace_id": basic_parameter["workspace_id"],
                   "project_name": basic_parameter["project_name"],
                   "artifact_name": config["artifact_name"],
                   "spec_raw": spec_raw}

        job_component = CreateJobComponent(st.session_state.windmill["client"],
                                           config["permission"],
                                           pipeline_params=config["parameters"],
                                           pipeline_param_keys={"job_name": "local_name",
                                                                "experiment_name": "job_experiment_name"})

        job_component.ok = is_ok
        job_component.render(request)

def render_st_advanced_parameters(key, parameters, defaults=[]):
    """
    render_st_advanced_parameters
    Args:
        key:
        parameters:
        defaults:

    Returns:

    """
    return render(key, parameters, defaults)

if __name__ == '__main__':
    main()
