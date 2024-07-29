# -*- coding: utf-8 -*-
"""
Copyright(C) 2024 baidu, Inc. All Rights Reserved

# @Time : 2024/6/4 15:04
# @Author : lidai@baidu.com
# @Email: lidai@baidu.com
# @File : st_render_pdc_example.py
# @Software: PyCharm
"""
from vistudiost.components import render_st_dataset, render_st_model, render_st_model_store, \
    render_st_endpoint_hub, render_st_compute, render_st_flavour, \
    render_st_deploy, render_st_create_job, render_st_package, \
    render_st_popup, render_st_advanced_parameters, render_st_model_detail
from vistudiost.components.create_job_component import CreateJobComponent
from vistudiost.pages.pipeline.base import get_spec_raw, \
    eval_part, transform_eval_part, inference_part
from vistudiost.components.advanced_parameter_component import get_advance_parameters
from windmillmodelv1.client.model_api_model import parse_model_name
from windmilltrainingv1.client.training_api_project import ProjectName
from vistudiost.pages.pipeline.base import set_pipeline_params
from vistudiost.utils.render import st_write, object_format, artifact_version_format, compute_format, find_index
from gaea_operator.utils.accelerator import get_accelerator
from vistudiost.cache.cache import get_project, get_pipeline, get_artifact, get_workspace_id, list_project
import bcelogger as logger
import streamlit as st
import re
from bceinternalsdk.client.paging import PagingRequest


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
                                    key="project_name")
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
                      key="project_name", disabled=True)
        project_name = config["project_name"]

    model_store_name, model_name, artifact_name = get_model_list_part(config)

    basic_param.update({"model_store_name": model_store_name})
    basic_param["pipeline_category"] = getattr(pipeline_resp, "category", {}).get("category", "")
    basic_param["pipeline_display_name"] = getattr(pipeline_resp, "displayName", "")
    basic_param["workspace_id"] = workspace_id
    basic_param["project_name"] = project_name
    return basic_param, basic_ok


def annotation_part(config,
                workspace_id,
                project_name,
                model_store_name,
                pipeline_display_name,
                pipeline_category,
                ):
    """
    模型训练
    Args:
        config:
        workspace_id
        project_name
        model_store_name
        pipeline_category
        pipeline_display_name

    Returns:

    """
    st.markdown("")
    st_write("数据挖掘", font_size=16)
    st.markdown("")
    annotation_paramters = {}
    input_dataset, ok_train_dataset = render_st_dataset(["输入数据集选择"],
                                                        request={
                                                            "workspace_id": workspace_id,
                                                            "project_name": project_name,
                                                            "categories": [pipeline_category]},
                                                        pipeline_param_keys={
                                                            "dataset_name": "train.train_dataset_name"},
                                                        pipeline_params=config["parameters"],
                                                        permission=config["permission"])
    annotation_paramters.update(input_dataset)

    output_dataset, ok_dataset = render_st_dataset(["输出数据集选择", "数据集选择"],
                                                   request={"workspace_id": workspace_id,
                                                            "project_name": project_name,
                                                            "categories": [pipeline_category]},
                                                   pipeline_param_keys={"dataset_name": "eval.dataset_name"},
                                                   pipeline_params=st.session_state.config["parameters"],
                                                   permission=st.session_state.config["permission"])

    annotation_paramters.update(output_dataset)

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
    annotation_paramters.update(compute_name)
    flavour_list = [
        {"name": "c8m32gpu1", "display_name": "CPU: 8核 内存: 32Gi GPU: 1卡"},
        {"name": "c8m32gpu2", "display_name": "CPU: 8核 内存: 32Gi GPU: 2卡"},
        {"name": "c16m64gpu2", "display_name": "CPU: 16核 内存: 64Gi GPU: 2卡"},
        {"name": "c16m32gpu4", "display_name": "CPU: 16核 内存: 32Gi GPU: 4卡"},
        {"name": "c16m64gpu4", "display_name": "CPU: 16核 内存: 64Gi GPU: 4卡"},
        {"name": "c32m96gpu4", "display_name": "CPU: 32核 内存: 96Gi GPU: 4卡"}]

    flavour_name, ok_flavour = render_st_flavour(["资源套餐"],
                                                 request={"name": "gpu", "flavour_list": flavour_list},
                                                 pipeline_param_keys={"flavour_name": "train.flavour"},
                                                 pipeline_params=config["parameters"],
                                                 permission=config["permission"])
    annotation_paramters.update(flavour_name)

    is_ok = ok_train_dataset and ok_compute and ok_flavour and ok_dataset
    return annotation_paramters, is_ok


def _modify_accelerator(accelerator: str):
    """
    根据给定的加速器类型，返回对应的修改后的加速器类型。如果加速器为"A10"，则返回"T4"；否则，直接返回原始的加速器类型。
    
    Args:
        accelerator (str): 需要进行修改的加速器类型，可以是"A10"或其他字符串。
    
    Returns:
        str: 返回修改后的加速器类型，如果原始加速器为"A10"，则返回"T4"；否则，直接返回原始的加速器类型。
    """
    if accelerator == "A10":
        return "T4"
    else:
        return accelerator


def icafe_part(config):
    """
    icafe 卡片信息同步
    Args:
        None
    Returns:
        Dict
        :param config:
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
                                         key=f"icafe_operator", max_chars=80, disabled=if_icafe_operator_disabled)
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
    """
    验证输入的ICafe ID是否合法，如果合法则返回对应的整数，否则返回None。
    支持以下两种格式：
        1. 纯数字形式，例如"1234567890"；
        2. "cv-algorithm-{number}"形式，其中{number}为一个正整数，例如"cv-algorithm-1234567890"。

    Args:
        icafe_id_input (str): ICafe ID的输入字符串，可以是纯数字或者包含"cv-algorithm-{number}"形式的字符串。

    Returns:
        Union[int, None]: 如果输入的ICafe ID合法，则返回对应的整数；如果不合法，则返回None。
    """
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
    """
    验证ICAFE操作员输入是否符合要求，返回True或None。

    Args:
        icafe_operator_input (str): ICAFE操作员的输入字符串，必须为非空字符串且只包含英文、数字和特殊符号（._-）。

    Returns:
        Union[bool, None]: 如果输入字符串符合要求，返回True；否则返回None。
    """
    pattern = r'^[a-zA-Z0-9]+([._-]?[a-zA-Z0-9]+)*$'

    # 使用正则表达式进行匹配
    if re.match(pattern, icafe_operator_input):
        return True
    else:
        return None


def get_parts(config, basic_parameter):
    """
    get_parts
    Args:
        config:
        basic_parameter:

    Returns:

    """
    annotation_parameter, annotation_ok = annotation_part(config,
                                              basic_parameter["workspace_id"],
                                              basic_parameter["project_name"],
                                              basic_parameter["model_store_name"],
                                              basic_parameter["pipeline_display_name"],
                                              basic_parameter["pipeline_category"],
                                              )

    icafe_parameter, icafe_ok = icafe_part(config)

    return annotation_parameter, annotation_ok, \
        icafe_parameter, icafe_ok


def dataannotation_part(config):
    """
    pdc 提交任务
    Args:
        None
    Returns:
        Dict
    """
    st.markdown("")
    st_write("标签列表文件", font_size=16)
    st.markdown("")

    config_paramerters = config['parameters']
    category_parameters = {}

    if_category_disabled = False
    category_config = ""
    if config_paramerters.get("category_config"):
        category_config = config_paramerters.get("category_config")
        if_category_disabled = True
    category_config = st.text_input(
        "*请输入标签文件内容，COCO、ImageNet标注格式id从0开始递增，Cityscapes标注格式id从1开始递增", value=category_config,
        max_chars=80, disabled=if_category_disabled)

    category_parameters["category_config"] = category_config
    category_config_ok = True
    if category_config == "":
        category_config_ok = False

    return category_parameters, category_config_ok


def list_ensemble_model(config, model_store_name, tags=None, category=""):
    """
    列出model
    """
    try:
        model_list = st.session_state.windmill["client"].list_model(
            config["workspace_id"],
            model_store_name,
            filter_param="-ensemble",
            tags=tags,
            categories=[category],
            page_request=PagingRequest(
                page_no=1,
                page_size=100,
                orderby="created_at",
                order="desc"))

        if model_list is None:
            return list()

        if model_list.totalCount == 0:
            return list()

        copy_list = list()
        for i in model_list.result:
            copy_list.append(i["localName"])
        return copy_list

    except Exception as e:
        st.session_state.spi_has_error = True
        st.error("list_model error: {}".format(e))
        return list()


def list_modelstore(config):
    """
    列出modelstore
    """
    try:
        model_store_list = st.session_state.windmill["client"].list_model_store(
            config["workspace_id"],
            page_request=PagingRequest(
                page_no=1,
                page_size=100,
                orderby="created_at",
                order="desc"))

        if model_store_list.totalCount == 0:
            return

        copy_list = list()
        for i in model_store_list.result:
            copy_list.append(i['localName'])

        return copy_list

    except Exception as e:
        st.session_state.spi_has_error = True
        st.error("list_modelstore error: {}".format(e))
        return list()


def list_artifact(object_name):
    """
    列出artifact
    """
    try:
        pipeline_list = st.session_state.windmill["client"].list_artifact(
            object_name,
            page_request=PagingRequest(
                page_no=1,
                page_size=100,
                orderby='created_at',
                order='desc'))

        if pipeline_list.totalCount == 0:
            return list()

        copy_list = list()
        for i in pipeline_list.result:
            copy_list.append(i["version"])
        return copy_list

    except Exception as e:
        st.session_state.spi_has_error = True
        st.error("list_artifact error: {}".format(e))
        return list()


def get_model_list_part(config):
    """
    获取模型列表部分，包括模型仓库、编排节点名称和版本。
    
    Args:
        config (dict): 配置字典，包含工作空间ID和其他相关信息。
    
    Returns:
        tuple (str, str, str): 返回三个元素的元组，分别是模型仓库名称（str），编排节点名称（str）和版本（str）。
    """
    model_store_name = st.selectbox("模型仓库:", list_modelstore(config), key='spi_train_model_store')
    model_name_list = list_ensemble_model(config, model_store_name)

    ensemble_model_name = st.selectbox(
        '编排节点名称:',
        options=model_name_list,
        key='chart_ensemble_model_name'
    )
    object_name = f'workspaces/{config["workspace_id"]}' \
                  f'/modelstores/{model_store_name}' \
                  f'/models/{ensemble_model_name}'
    ensemble_model_version = st.selectbox(
        '编排节点版本:',
        list_artifact(object_name),
        key='chart_ensemble_model_version')

    return model_store_name, ensemble_model_name, ensemble_model_version


def main():
    """
    Args:
    Returns:

    """
    config = st.session_state.config
    set_pipeline_params()

    basic_parameter, basic_ok = basic_part(config)

    annotation_parameter, annotation_ok, \
        icafe_parameters, icafe_ok = get_parts(config, basic_parameter)

    parameters = {}
    parameters.update(annotation_parameter)
    parameters.update(icafe_parameters)

    parameters["windmill_ak"] = st.session_state.windmill["client"].config.credentials.access_key_id.decode('utf-8')
    parameters["windmill_sk"] = st.session_state.windmill["client"].config.credentials.secret_access_key.decode('utf-8')
    parameters["windmill_endpoint"] = st.secrets.windmill.endpoint
    project_name = ProjectName(workspace_id=basic_parameter["workspace_id"], local_name=basic_parameter["project_name"])
    parameters["project_name"] = project_name.get_name()
    parameters["model_store_name"] = basic_parameter["model_store_name"]

    artifact_resp = get_artifact(st.session_state.windmill["client"], st.session_state.config["artifact_name"])
    if getattr(artifact_resp, "tags") and artifact_resp.tags.get("scene"):
        parameters["scene"] = artifact_resp.tags.get("scene")
    is_ok = basic_ok and annotation_ok and icafe_ok

    if config["permission"] == "readwrite":
        request = {"parameters": parameters,
                   "version": config["version"],
                   "object_name": config["object_name"],
                   "pipeline": config["pipeline_name"],
                   "workspace_id": basic_parameter["workspace_id"],
                   "project_name": basic_parameter["project_name"],
                   "artifact_name": config["artifact_name"],
                   }

        job_component = CreateJobComponent(st.session_state.windmill["client"],
                                           config["permission"],
                                           pipeline_params=config["parameters"],
                                           pipeline_param_keys={"job_name": "local_name",
                                                                "experiment_name": "job_experiment_name"})

        job_component.ok = is_ok
        job_component.render(request)


if __name__ == '__main__':
    main()
