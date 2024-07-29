# -*- coding: utf-8 -*-
"""
Copyright(C) 2024 baidu, Inc. All Rights Reserved

# @Time : 2024/6/4 15:04
# @Author : lidai@baidu.com
# @Email: lidai@baidu.com
# @File : st_render.py
# @Software: PyCharm
# @Description: 数据挖掘微界面
"""
import pdb

from bceinternalsdk.client.validator import local_name as local_name_validator
from windmillartifactv1.client.artifact_api_artifact import parse_artifact, get_name as get_dataset_name
from windmillcomputev1.client.compute_api_compute import parse_compute_name
from windmillmodelv1.client.model_api_modelstore import parse_modelstore_name
from windmilltrainingv1.client.training_api_project import ProjectName
from vistudiost.cache.cache import list_items, list_artifact, get_compute, suggest_first_compute, \
    list_model_store, get_model_store
from vistudiost.utils.random import random_string
from vistudiost.cache.cache import create_job
from vistudiost.components.base_component import WindmillComponent
from vistudiost.pages.pipeline.base import set_pipeline_params
from vistudiost.utils.render import st_write, compute_format, find_index
from vistudiost.cache.cache import get_project, get_pipeline, get_artifact
import streamlit as st
import re
from bceinternalsdk.client.paging import PagingRequest
from windmillclient.client.windmill_client import WindmillClient

label_format_coco = 'COCO'
label_format_image_net = 'ImageNet'
label_format_cityscapes = 'Cityscapes'


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

    workspace_id = config["workspace_id"]
    response = get_project(st.session_state.windmill["client"],
                           request={"workspace_id": workspace_id,
                                    "project_name": config["project_name"]})
    basic_param["project_name"] = getattr(response, "name", "")
    project_name = config["project_name"]
    icafe_parameter, icafe_ok = icafe_part(config)

    basic_param["pipeline_category"] = getattr(pipeline_resp, "category", {}).get("category", "")
    basic_param["pipeline_display_name"] = getattr(pipeline_resp, "displayName", "")
    basic_param["workspace_id"] = workspace_id
    basic_param["project_name"] = project_name
    basic_param.update(icafe_parameter)
    return basic_param, basic_ok and icafe_ok


def mining_part(config,
                workspace_id,
                project_name,
                pipeline_category):
    """
    模型训练
    Args:
        config:
        workspace_id
        project_name
        pipeline_category

    Returns:

    """
    st.markdown("")
    st_write("数据挖掘", font_size=16)
    st.markdown("")

    config_parameters = config['parameters']
    mining_parameters = {}

    # select model which used to deploy
    model_store_name_dict, ok_model_store = render_st_model_store(["模型仓库"],
                                                                  request={
                                                                      "workspace_id": workspace_id},
                                                                  pipeline_param_keys={
                                                                      "model_store_name": "model_store_name"},
                                                                  pipeline_params=config["parameters"],
                                                                  permission=config["permission"])
    selected_ensemble_model, ok_model = render_st_model(["选择模型"],
                                                        pipeline_param_keys={
                                                            "model_name": "model_name",
                                                            "model_display_name": "model_display_name"},
                                                        pipeline_params=config["parameters"],
                                                        request={
                                                            "model_store_name": model_store_name_dict[
                                                                'model_store_name'],
                                                            "workspace_id": workspace_id,
                                                            "categories": [pipeline_category]},
                                                        permission=config["permission"])

    flavour_parameter = {'flavour': 'c8m32gpu1'}
    mining_docker_env_parameter = {"mining_env": "iregistry.baidu-int.com/windmill-public/inference"
                                                 "/triton_r22_12_nvidia_infer_trt86:1.3.2.3-datamining-dist1"}
    # 当模型为多模态模型时，增加对应标识，
    # flavour 改为 32 核 96 G 4 卡
    # 使用多模态大模型专用镜像
    if "model_name" in selected_ensemble_model:
        mining_parameters.update(selected_ensemble_model)
        if ('tags' in selected_ensemble_model["model_name"]["artifact"] and
                'modelExtraSpecific' in selected_ensemble_model["model_name"]["artifact"]['tags'] and
                selected_ensemble_model["model_name"]["artifact"]['tags']['modelExtraSpecific'] == "Multimodal"):
            mining_docker_env_parameter["mining_env"] = "iregistry.baidu-int.com/acg_aiqp_algo/cv-dev/ivl:v0.1-dev6"
            flavour_parameter = {'flavour': 'c32m96gpu4'}

    mining_parameters.update(model_store_name_dict)

    mining_parameters.update(mining_docker_env_parameter)
    mining_parameters.update(flavour_parameter)

    input_datasets, ok_input_datasets = render_st_dataset(["源数据集"],
                                                          request={
                                                              "workspace_id": workspace_id,
                                                              "project_name": project_name,
                                                              "categories": [pipeline_category]},
                                                          pipeline_param_keys={
                                                              "dataset_name": "input_dataset_name"},
                                                          pipeline_params=config["parameters"],
                                                          permission=config["permission"])
    mining_parameters.update(input_datasets)

    mining_key_word_val = ""
    if_mining_key_word_val_disabled = False
    if config_parameters.get("mining_key_word"):
        mining_key_word_val = config_parameters.get("mining_key_word")
        if_mining_key_word_val_disabled = True

    mining_key_word = st.text_input(f':red[*]挖掘关键词',
                                    value=mining_key_word_val,
                                    key="mining_key_word", max_chars=80, disabled=if_mining_key_word_val_disabled)
    mining_parameters.update({"mining_key_word": mining_key_word})

    mining_key_word_description_val = ""
    if_mining_key_word_val_description_disabled = False
    if config_parameters.get("mining_key_word_description"):
        mining_key_word_description_val = config_parameters.get("mining_key_word_description")
        if_mining_key_word_val_description_disabled = True
    mining_key_word_description = st.text_input(f'关键词描述',
                                                value=mining_key_word_description_val,
                                                key="mining_key_word_description", max_chars=200,
                                                disabled=if_mining_key_word_val_description_disabled)
    if mining_key_word_description:
        mining_parameters.update({"mining_key_word_description": mining_key_word_description})

    option_dict = {
        "分类": "classify",
        "检测": "detect"
    }
    selected_option = st.selectbox(f':red[*]挖掘模型', list(option_dict.keys()))
    mining_algorithm = option_dict[selected_option]
    mining_parameters.update({"mining_algorithm": mining_algorithm})

    output_dataset_name = ""
    if config['parameters'].get("output_dataset_name"):
        output_dataset_name = config['parameters'].get("output_dataset_name")
    output_dataset_display_name = st.text_input(f':red[*]产出数据集名称',
                                                value=output_dataset_name,
                                                key="output_dataset_name", max_chars=80)
    ok_output_datasets = True
    if output_dataset_display_name == "":
        ok_output_datasets = False
    mining_parameters.update({"output_dataset_name": output_dataset_display_name})

    annotation_type = st.selectbox(
        "预测结果格式:", [label_format_coco, label_format_image_net, label_format_cityscapes],
        key='annotation_type'
    )
    mining_parameters.update({"annotation_type": annotation_type})

    if_threshold_disabled = False
    label_confidence_threshold = ""
    if config['parameters'].get("label_confidence_data"):
        label_confidence_threshold = config['parameters'].get("label_confidence_data")
        if_threshold_disabled = True

    label_confidence_threshold = st.text_input("标签过滤条件", label_confidence_threshold,
                                               key=f"label_confidence_threshold", max_chars=1000,
                                               disabled=if_threshold_disabled)
    if label_confidence_threshold:
        mining_parameters.update({"label_confidence_threshold": label_confidence_threshold})

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
    mining_parameters.update(compute_name)

    is_ok = ok_output_datasets and ok_compute and mining_key_word
    return mining_parameters, is_ok


def render_st_compute(labels,
                      request,
                      client=None,
                      pipeline_param_keys=None,
                      pipeline_params=None,
                      permission=None):
    """
    render_st_compute
    Args:
        labels:
        client:
        request:
        pipeline_param_keys:
        pipeline_params:
        permission:

    Returns:

    """

    return ComputeComponent(labels,
                            client,
                            permission,
                            pipeline_params,
                            pipeline_param_keys).render(request)


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
    config_parameters = config['parameters']
    icafe_parameters = {}
    is_icafe_ok = True

    if_icafe_id_disabled = False
    icafe_id = ""
    if config_parameters.get("icafe_id"):
        icafe_id = config_parameters.get("icafe_id")
        if_icafe_id_disabled = True

    icafe_id = st.text_input("[必填]卡片 ID", icafe_id, key=f"icafe_id", max_chars=80, disabled=if_icafe_id_disabled)
    if not validate_icafe_id_input(icafe_id):
        is_icafe_ok = False
        st.error("请输入正确的卡片 ID，支持仅输入卡片数字编号（如 477 ）或完整卡片名称（如 cv-algorithm-477 ）")

    icafe_parameters["icafe_id"] = icafe_id

    if_icafe_operator_disabled = False
    icafe_operator = ""
    if config_parameters.get("icafe_operator"):
        icafe_operator = config_parameters.get("icafe_operator")
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
    icafe_parameters["icafe_operator"] = icafe_operator_input

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
    mining_parameter, mining_ok = mining_part(config,
                                              basic_parameter["workspace_id"],
                                              basic_parameter["project_name"],
                                              basic_parameter["pipeline_category"],
                                              )

    return mining_parameter, mining_ok


def list_ensemble_model(workspace_id, model_store_name, tags=None, category=""):
    """
    列出model
    """
    try:
        model_list = st.session_state.windmill["client"].list_model(
            workspace_id,
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

        model_artifact_list = list()
        model_local_name_list = list()
        for i in model_list.result:
            model_local_name_list.append(i["localName"])
            model_artifact_list.append(i)
        return model_local_name_list, model_artifact_list

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
            copy_list.append(i['displayName'])

        return copy_list

    except Exception as e:
        st.session_state.spi_has_error = True
        st.error("list_modelstore error: {}".format(e))
        return list()


def main():
    """
    Args:
    Returns:

    """
    config = st.session_state.config
    set_pipeline_params()

    basic_parameter, basic_ok = basic_part(config)

    mining_parameter, mining_ok = get_parts(config, basic_parameter)

    parameters = {}
    parameters.update(basic_parameter)
    parameters.update(mining_parameter)

    # get model artifact name from model selector
    model_artifact = ""
    if "model_name" in parameters:
        model_artifact = parameters["model_name"]
        parameters["model_name"] = model_artifact["name"]
        parameters["model_artifact_version"] = str(model_artifact["artifact"]["version"])

    if "model_display_name" in parameters:
        del parameters["model_display_name"]

    # get windmill ak sk
    parameters["windmill_ak"] = st.session_state.windmill["client"].config.credentials.access_key_id.decode('utf-8')
    parameters["windmill_sk"] = st.session_state.windmill["client"].config.credentials.secret_access_key.decode('utf-8')
    parameters["windmill_endpoint"] = st.secrets.windmill.endpoint
    project_name = ProjectName(workspace_id=basic_parameter["workspace_id"], local_name=basic_parameter["project_name"])
    parameters["project_name"] = project_name.get_name()

    artifact_resp = get_artifact(st.session_state.windmill["client"], st.session_state.config["artifact_name"])
    if getattr(artifact_resp, "tags") and artifact_resp.tags.get("scene"):
        parameters["scene"] = artifact_resp.tags.get("scene")
    is_ok = basic_ok and mining_ok

    print(f"=======job parameters==========={parameters}")
    if config["permission"] == "readwrite":
        request = {"parameters": parameters,
                   "object_name": config["object_name"],
                   "pipeline": config["pipeline_name"],
                   "workspace_id": basic_parameter["workspace_id"],
                   "project_name": basic_parameter["project_name"],
                   "artifact_name": config["artifact_name"],
                   "pipeline_category": basic_parameter["pipeline_category"],
                   "model_store_name": mining_parameter["model_store_name"],
                   }
        job_component = CreateJobComponent(st.session_state.windmill["client"],
                                           config["permission"],
                                           pipeline_params=config["parameters"],
                                           pipeline_param_keys={"job_name": "local_name",
                                                                "experiment_name": "job_experiment_name"})
        job_component.ok = is_ok
        job_component.render(request)


class CreateJobComponent(WindmillComponent):
    """
    JobComponent
    """

    def __init__(self, client,
                 permission,
                 pipeline_params={},
                 pipeline_param_keys=None):
        """
        JobComponent
        Args:
            client:
        """
        super(CreateJobComponent, self).__init__(client=client,
                                                 pipeline_params=pipeline_params,
                                                 permission=permission)
        if pipeline_param_keys is None:
            pipeline_param_keys = {"job_name": "job_local_name", "experiment_name": "experiment_name"}
        self.job_key = pipeline_param_keys["job_name"]
        self.experiment_key = pipeline_param_keys["experiment_name"]

    def render_with_readwrite(self, request):
        """
        渲染界面
        Args:

        Returns:

        """
        st.markdown("")
        st_write("创建作业", font_size=18)
        st.markdown("")
        st_write("基本配置", font_size=16)
        if "random_job_name" not in st.session_state:
            st.session_state['random_job_name'] = "job" + random_string()
        display_name = st.text_input(
            '作业名称',
            max_chars=100,
            value=self.pipeline_params.get("display_name", ""),
            key=f"{self.job_key} + _display_name"
        )

        local_name = st.session_state.get('random_job_name', "")

        request["display_name"] = display_name
        request["local_name"] = local_name
        if local_name == "":
            st.error("请填写作业名称")
            self.ok = False
        if local_name:
            if not local_name_validator(local_name):
                self.show_error('任务名称仅以字母或下划线 "_" 开头，后续可以包含字母、数字、连字符 "-"')
            else:
                st.session_state['random_job_name'] = local_name
        description = st.text_input(
            '作业描述',
            max_chars=255,
            placeholder="请输入作业描述",
            value=self.pipeline_params.get("description", ""),
            key="job_description")
        request["description"] = description

        st.session_state['random_experiment_name'] = 'exp' + random_string()
        experiment_name = st.session_state['random_experiment_name']
        if experiment_name:
            if not local_name_validator(experiment_name):
                self.show_error('实验名称仅以字母或下划线 "_" 开头，后续可以包含字母、数字、连字符 "-"')
                self.ok = False
        request["experiment_name"] = experiment_name
        if st.button("创建任务", key="job_start", disabled=not self.ok, use_container_width=True):
            if request["local_name"] != "" and request["experiment_name"] != "":
                response = create_job(self.client, request)
                if response.message:
                    st.toast(f'创建失败: {response.message} 请稍后重试')

                else:
                    st.toast(f'创建成功，请至『作业管理』查看作业详情')

    def render_with_readonly(self):
        """
        渲染界面
        Args:

        Returns:

        """
        return


def render_st_model_store(labels,
                          request,
                          client=None,
                          pipeline_param_keys=None,
                          pipeline_params=None,
                          permission=None):
    """
    render_st_model_store
    Args:
        labels:
        client:
        request:
        pipeline_param_keys:
        pipeline_params:
        permission:

    Returns:

    """
    return ModelStoreComponent(labels,
                               client,
                               permission,
                               pipeline_params,
                               pipeline_param_keys).render(request)


class ModelStoreComponent(WindmillComponent):
    """
    ModelStoreComponent
    """

    def __init__(self, labels, client,
                 permission,
                 pipeline_params={},
                 pipeline_param_keys=None):
        """
        ModelStoreComponent
        Args:
            client:
        """
        super(ModelStoreComponent, self).__init__(client=client,
                                                  pipeline_params=pipeline_params,
                                                  permission=permission)
        self.labels = labels
        if pipeline_param_keys is None:
            pipeline_param_keys = {"model_store_name": "MODEL_STORE_NAME"}
        self.model_store_name_key = pipeline_param_keys["model_store_name"]

    def render_with_readonly(self):
        """
        渲染界面
        Returns:

        """
        model_store_name = parse_modelstore_name(self.pipeline_params[self.model_store_name_key])
        if model_store_name is not None:
            model_store_resp = get_model_store(self.client, model_store_name)
        model_store_selected = st.selectbox(
            f':red[*]{self.labels[0]}: ',
            options=[model_store_resp],
            format_func=object_format,
            key=self.model_store_name_key
        )

        return {self.model_store_name_key: self.pipeline_params[self.model_store_name_key]}, self.ok

    def render_with_readwrite(self, request):
        """
        渲染界面
        Args:

        Returns:

        """
        if request.get("model_store_name") is not None:
            model_store_name = parse_modelstore_name(request.get("model_store_name"))
            model_store_resp = get_model_store(self.client, model_store_name)
            model_store_selected = st.text_input(
                f':red[*]{self.labels[0]}: ',
                value=object_format(model_store_resp.__dict__),
                key=self.model_store_name_key,
                disabled=True
            )
            return {self.model_store_name_key: model_store_resp.__dict__["name"]}, self.ok

        model_store_list = list_model_store(self.client, request)

        model_store_selected = st.selectbox(
            f':red[*]{self.labels[0]}: ',
            options=model_store_list,
            format_func=object_format,
            key=self.model_store_name_key,
            index=find_index(model_store_list, "name", self.pipeline_params.get(self.model_store_name_key, ""))
        )
        if model_store_selected is None:
            st.error("请选择模型仓库")
            self.ok = False

        return {self.model_store_name_key: model_store_selected["name"]}, self.ok


def render_st_dataset(labels,
                      request,
                      client=None,
                      pipeline_param_keys=None,
                      pipeline_params=None,
                      permission=None):
    """
    render_st_dataset
    Args:
        labels:
        client:
        request:
        pipeline_param_keys:
        pipeline_params:
        permission:

    Returns:

    """
    return DatasetComponent(labels,
                            client,
                            permission,
                            pipeline_params,
                            pipeline_param_keys).render(request)


# override DatasetComponent
class DatasetComponent(WindmillComponent):
    """
    DatasetComponent
    """

    def __init__(self, labels, client,
                 permission,
                 pipeline_params={},
                 pipeline_param_keys=None):
        """
        DatasetComponent
        Args:
            client:
        """
        super(DatasetComponent, self).__init__(client=client,
                                               pipeline_params=pipeline_params,
                                               permission=permission)
        self.labels = labels
        if pipeline_param_keys is None:
            pipeline_param_keys = {"dataset_name": "WINDMILL_DATASET_NAME"}
        self.dataset_name_key = pipeline_param_keys["dataset_name"]

    def render_with_readonly(self):
        """
        渲染界面
        Returns:

        """
        dataset_col = st.columns([4])[0]  # 只需要一个列，所以只定义一个列

        pre_dataset_object_name = ""
        pre_dataset_version = ""
        if self.pipeline_params.get(self.dataset_name_key):
            pre_dataset_object_name = parse_artifact(self.pipeline_params.get(self.dataset_name_key)).naming.object_name
            pre_dataset_version = str(parse_artifact(self.pipeline_params.get(self.dataset_name_key)).version)

        with dataset_col:
            dataset_list = list_dataset(self.client, self.pipeline_params)

            # 获取所有数据集和版本的组合
            dataset_version_list = []
            for dataset in dataset_list:
                artifact_list = list_artifact(self.client, dataset['name'])
                for artifact in artifact_list:
                    display_name = f"{dataset['displayName']} (v{artifact['version']})"
                    dataset_version_list.append((display_name, dataset['name'], artifact['version']))

            # 查找预选的索引
            pre_selected = f"{pre_dataset_object_name} (v{pre_dataset_version})"
            index = next((i for i, (name, _, version) in enumerate(dataset_version_list) if
                          f"{name} (v{version})" == pre_selected), 0)

            # 创建选择框
            selected_option = st.selectbox(
                f':red[*]{self.labels[0]}:',
                options=dataset_version_list,
                format_func=lambda x: x[0],  # 只显示名称+版本
                key=self.dataset_name_key,
                index=index
            )

            if not selected_option:
                st.error("请选择源数据集")
                self.ok = False
                return {self.dataset_name_key: ''}, self.ok

        # 解析选中的数据集名称和版本
        selected_name = selected_option[1]
        selected_version = selected_option[2]

        return {self.dataset_name_key: get_dataset_name(selected_name, selected_version)}, self.ok

    def render_with_readwrite(self, request):
        """
        渲染界面
        Args:

        Returns:

        """
        dataset_col = st.columns([4])[0]  # 只需要一个列，所以只定义一个列

        pre_dataset_object_name = ""
        pre_dataset_version = ""
        if self.pipeline_params.get(self.dataset_name_key):
            pre_dataset_object_name = parse_artifact(self.pipeline_params.get(self.dataset_name_key)).naming.object_name
            pre_dataset_version = str(parse_artifact(self.pipeline_params.get(self.dataset_name_key)).version)

        with dataset_col:
            dataset_list = list_dataset(self.client, request)

            # 获取所有数据集和版本的组合
            dataset_version_list = []
            for dataset in dataset_list:
                artifact_list = list_artifact(self.client, dataset['name'])
                for artifact in artifact_list:
                    display_name = f"{dataset['displayName']} (v{artifact['version']})"
                    dataset_version_list.append((display_name, dataset['name'], artifact['version']))

            # 查找预选的索引
            pre_selected = f"{pre_dataset_object_name} (v{pre_dataset_version})"
            pre_selected_indices = [i for i, (name, _, version) in enumerate(dataset_version_list) if
                                    f"{name} (v{version})" == pre_selected]

            # 创建多选框
            selected_options = st.multiselect(
                f':red[*]{self.labels[0]}:',
                options=dataset_version_list,
                format_func=lambda x: x[0],  # 只显示名称+版本
                default=[dataset_version_list[i] for i in pre_selected_indices],
                key=self.dataset_name_key
            )

            if not selected_options:
                st.error("请选择数据集")
                self.ok = False
                return {self.dataset_name_key: ''}, self.ok

        # 解析选中的数据集名称和版本
        selected_names_versions = [(option[1], option[2]) for option in selected_options]

        return {self.dataset_name_key: [get_dataset_name(name, version) for name, version in
                                        selected_names_versions]}, self.ok


class ComputeComponent(WindmillComponent):
    """
    ComputeComponent
    """

    def __init__(self, labels, client,
                 permission,
                 pipeline_params={},
                 pipeline_param_keys=None):
        """
        ComputeComponent
        Args:
            client:
        """
        super(ComputeComponent, self).__init__(client=client,
                                               pipeline_params=pipeline_params,
                                               permission=permission)
        self.labels = labels
        if pipeline_param_keys is None:
            pipeline_param_keys = {"compute_name": "compute_name"}
        self.compute_name_key = pipeline_param_keys["compute_name"]

    def render_with_readonly(self):
        """
        渲染界面
        Returns:

        """
        compute_name = parse_compute_name(self.pipeline_params[self.compute_name_key])
        compute = get_compute(self.client, compute_name)
        compute_selected = st.selectbox(
            f':red[*]{self.labels[0]}: ',
            options=[compute_format(compute)],
            key=self.compute_name_key
        )

        return {self.compute_name_key: self.pipeline_params[self.compute_name_key]}, self.ok

    def render_with_readwrite(self, request):
        """
        渲染界面
        Args:

        Returns:

        """

        if request.get("compute_name"):
            compute_name = parse_compute_name(request["compute_name"])
            compute_resp = get_compute(self.client, compute_name)
            compute_list = [compute_resp.__dict__]
        else:
            compute_list = suggest_first_compute(self.client, request)

        compute_selected = compute_list[0]
        if compute_selected is None:
            st.error("计算资源获取失败，请联系管理员！")
            self.ok = False
            return {self.compute_name_key: None}, self.ok

        return {self.compute_name_key: compute_selected["name"]}, self.ok


def render_st_model(labels,
                    request,
                    client=None,
                    pipeline_param_keys=None,
                    pipeline_params=None,
                    permission=None):
    """
    render_st_model
    Args:
        labels:
        client:
        request:
        pipeline_param_keys:
        pipeline_params:
        permission:

    Returns:

    """
    return ModelComponent(labels,
                          client,
                          permission,
                          pipeline_params,
                          pipeline_param_keys).render(request)


class ModelComponent(WindmillComponent):
    """
    ModelComponent
    """

    def __init__(self, labels, client,
                 permission,
                 pipeline_params={},
                 pipeline_param_keys=None):
        """
        ModelComponent
        Args:
            client:
        """
        super(ModelComponent, self).__init__(client=client,
                                             pipeline_params=pipeline_params,
                                             permission=permission)
        self.labels = labels
        if pipeline_param_keys is None:
            pipeline_param_keys = {"model_name": "MODEL_NAME",
                                   "model_artifact_name": "MODEL_ARTIFACT_NAME",
                                   "model_display_name": "train.MODEL_DISPLAYNAME_NAME"}
        self.model_name_key = pipeline_param_keys["model_name"]
        self.display_name_key = pipeline_param_keys["model_display_name"]

    def render_with_readonly(self):
        """
        渲染界面
        Returns:

        """
        config = {}

        if parse_modelstore_name(self.pipeline_params["model_store_name"]) is not None:
            model_store_name = parse_modelstore_name(self.pipeline_params["model_store_name"]).local_name

            model_local_name_list, model_artifact_list = list_ensemble_model(self.pipeline_params["workspace_id"],
                                                                             model_store_name)

            if self.pipeline_params.get(self.model_name_key):
                model_artifact_name = self.pipeline_params.get(self.model_name_key) + "/versions/" + \
                                      self.pipeline_params["model_artifact_version"]
                index = find_model_index(model_artifact_list, "name", model_artifact_name)
            else:
                index = next((i + 1 for i, model in enumerate(model_local_name_list)
                              if hasattr(model, 'name') and model.name == self.pipeline_params.get("model_name")), 0)

            model_name = st.selectbox(
                f':red[*]选择挖掘模型包:',
                options=model_artifact_list,
                format_func=object_format,
                key=self.model_name_key,
                index=index
            )
            if model_name is None:
                st.error('没有模型可供选择')
                self.ok = False
                return {self.model_name_key: "", self.display_name_key: ""}, self.ok

        return config, self.ok

    def render_with_readwrite(self, request):
        """
        渲染界面
        Args:

        Returns:

        """
        if request["model_store_name"] is not None:
            if parse_modelstore_name(request["model_store_name"]) is not None:
                request["model_store_name"] = parse_modelstore_name(request["model_store_name"]).local_name

            ensemble_model_list = list_ensemble_model(request["workspace_id"],
                                                      request["model_store_name"])
            if len(ensemble_model_list) == 2:
                model_local_name_list, model_artifact_list = ensemble_model_list
            else:
                model_local_name_list, model_artifact_list = [], []

            if self.pipeline_params.get(self.model_name_key):
                index = find_index(model_local_name_list, "name", self.pipeline_params.get(self.model_name_key))
            else:
                index = next((i + 1 for i, model in enumerate(model_local_name_list)
                              if hasattr(model, 'name') and model.name == request.get("model_name")), 0)

            model_name = st.selectbox(
                f':red[*]选择挖掘模型包:',
                options=model_artifact_list,
                format_func=object_format,
                key=self.model_name_key,
                index=index
            )
            if model_name is None:
                st.error('没有模型可供选择')
                self.ok = False
                return {self.model_name_key: "", self.display_name_key: ""}, self.ok

            display_name = model_name
            if self.pipeline_params.get(self.display_name_key):
                display_name = self.pipeline_params.get(self.display_name_key)

            return {
                self.model_name_key: model_name,
                self.display_name_key: display_name,
            }, self.ok


def find_model_index(result_list, name_key, value):
    """
    判断变量在列表中的索引
    Args:
        result_list:
        name_key:
        value:

    Returns:

    """
    if value == "":
        return 0
    if not isinstance(result_list, (list, tuple, set, dict)):
        return 0
    for index, result in enumerate(result_list):
        if result.get('artifact', "").get('name') == value:
            return index
    return 0


def object_format(obj):
    """
    格式化对象
    Args:
        obj:
    """
    if obj is None or obj == "" or obj == {} or obj == []:
        return ''
    if isinstance(obj, dict):
        display_name = obj.get('displayName', '')
        artifact = obj.get('artifact', '')
        version = ""
        if artifact:
            version = artifact.get('version', '')
    else:
        display_name = getattr(obj, 'displayName', '')
        artifact = getattr(obj, 'artifact', '')
        version = getattr(artifact, 'version', '')
    return str(display_name) + "(v" + str(version) + ")" if version != "" else display_name


def list_dataset(client: WindmillClient, request):
    """
    list dataset
    Args:
        client:
        request:
    """
    return list_items(client, client.list_dataset,
                      workspace_id=request["workspace_id"],
                      project_name=request["project_name"]
                      )


if __name__ == '__main__':
    main()
