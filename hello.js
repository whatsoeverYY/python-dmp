export const enum E_ROLE {
  /**
   * 超级管理员
   */
  SYSTEM_ADMIN = 'system_admin',
  /**
   * 数据维护人员
   */
  DATA_MAINTAIN = 'data_maintain',
  /**
   * 审批员
   */
  DATA_APPROVE = 'data_approve',
}

export const enum E_ERROR_CODE {
  BAD_REQUEST = 'errors.com.patsnap.service',
  BAD_REQUEST_WARNING = 'errors.com.patsnap.service.warning',
}
export const enum E_PERMISSION {
  /* ---------------------------------- 列表按钮 ---------------------------------- */
  /** 流程图 */
  WORKFLOW = 'WORKFLOW',
  /** 查看 */
  PREVIEW = 'PREVIEW',
  /** 预览 */
  PREVIEW_COMPARISON = 'PREVIEW_COMPARISON',
  /** 编辑 */
  EDIT = 'EDIT',
  /** 删除 */
  DELETE = 'DELETE',
  /** 撤回 */
  WITHDRAW = 'WITHDRAW',
  /** 驳回 */
  TURNDOWN = 'TURNDOWN',
  /** 提交发布 */
  APPROVE = 'APPROVE',
  /** 提交发布 */
  APPROVE_LIST = 'APPROVE_LIST',
  /** 发布 */
  PUBLISH = 'PUBLISH',
  /** 下架 */
  OFFLINE = 'OFFLINE',
  /** 恢复 */
  RESTORE = 'RESTORE',
  /** 标注 */
  ANNOTATION = 'ANNOTATION',
  /** 查看标注 */
  PREVIEW_ANNOTATION = 'PREVIEW_ANNOTATION',
  /** 编辑父节点 */
  UPDATE_PARENT = 'UPDATE_PARENT',
  /** 搜索当前记录 */
  SEARCH_CURRENT_ITEM = 'SEARCH_CURRENT_ITEM',

  /* ---------------------------------- 详情按钮 ---------------------------------- */

  /** 保存 */
  SAVE = 'SAVE',
  /** 保存全部 */
  SAVE_ALL = 'SAVE_ALL',
  /** 返回 */
  BACK = 'BACK',
  /** 取消 */
  CANCEL = 'CANCEL',
  /** 提交审核 */
  POST_FOR_REVIEW = 'POST_FOR_REVIEW',
  /** 列表提交审核 */
  POST_FOR_LIST_REVIEW = 'POST_FOR_LIST_REVIEW',
  /** 提交并发布 */
  POST_AND_APPROVE = 'POST_AND_APPROVE',
  /** 关联公司 */
  CONNECT_COMPANY = 'CONNECT_COMPANY',
  /** 关联药物 */
  CONNECT_DRUG = 'CONNECT_DRUG',
  /** 关联适应症 */
  CONNECT_DISEASE = 'CONNECT_DISEASE',
  /** 查阅记录 */
  REVIEW_RECORDS = 'REVIEW_RECORDS',
  /** 检查 */
  CHECK = 'CHECK',
  /** 复制 */
  COPY = 'COPY',
  /** 同步 */
  SYNC = 'SYNC',
  /* -------------------------------------------- DRUG_STRUCTURE -------------------------------------------- */
  /** 加入人工来源 */
  COPY_TO_MANUAL_SOURCE = 'COPY_TO_MANUAL_SOURCE',
  /** 软删除 */
  SOFT_DELETE = 'SOFT_DELETE',
  /* -------------------------------- Pipeline -------------------------- */
  DISABLE = 'DISABLE',
  ENABLE = 'ENABLE',
  /** 核实 */
  PIPELINE_CHECK = 'PIPELINE_CHECK',
  /** 信息登记 */
  PIPELINE_REGISTER = 'PIPELINE_REGISTER',
  /** 提交验收 */
  PIPELINE_SUBMIT_REGISTER = 'PIPELINE_SUBMIT_REGISTER',
  /** 驳回验收 */
  PIPELINE_REJECT_REGISTER = 'PIPELINE_REJECT_REGISTER',
  /** 验收 */
  PIPELINE_SAVE_REGISTER = 'PIPELINE_SAVE_REGISTER',
  /** 历史 */
  PIPELINE_HISTORY = 'PIPELINE_HISTORY',
  /** 有变化 */
  PIPELINE_CHANGE = 'PIPELINE_CHANGE',
  /** 无变化 */
  PIPELINE_NO_CHANGE = 'PIPELINE_NO_CHANGE',

  /**
   * 查看流程图
   */
  // PREVIEW_WORKFLOW = 'PREVIEW_WORKFLOW',
  // PREVIEW_IN_EDITING = 'PREVIEW_IN_EDITING',
  // EDIT_IN_EDITING = 'EDIT_IN_EDITING',
  // DELETE_IN_EDITING = 'DELETE_IN_EDITING',

  // PREVIEW_IN_TO_REVIEW = 'PREVIEW_IN_TO_REVIEW',
  // WITHDRAW_IN_TO_REVIEW = 'WITHDRAW_IN_TO_REVIEW',
  // TURNDOWN_IN_TO_REVIEW = 'TURNDOWN_IN_TO_REVIEW',
  // DELETE_IN_TO_REVIEW = 'DELETE_IN_TO_REVIEW',
  // APPROVE_IN_TO_REVIEW = 'APPROVE_IN_TO_REVIEW',
  // EDIT_IN_TO_REVIEW = 'EDIT_IN_TO_REVIEW',

  // PREVIEW_IN_TO_RELEASE = 'PREVIEW_IN_TO_RELEASE',
  // DELETE_IN_TO_RELEASE = 'DELETE_IN_TO_RELEASE',
  // PUBLISH_IN_TO_RELEASE = 'PUBLISH_IN_TO_RELEASE',
  // TURNDOWN_IN_TO_RELEASE = 'REJECT_IN_TO_RELEASE',

  // PREVIEW_IN_REJECT = 'PREVIEW_IN_REJECT',
  // EDIT_IN_REJECT = 'EDIT_IN_REJECT',
  // DELETE_IN_REJECT = 'DELETE_IN_REJECT',

  // PREVIEW_IN_ACTIVE = 'PREVIEW_IN_ACTIVE',
  // EDIT_IN_ACTIVE = 'EDIT_IN_ACTIVE',
  // OFFLINE_IN_ACTIVE = 'OFFLINE_IN_ACTIVE',
  // DELETE_IN_ACTIVE = 'DELETE_IN_ACTIVE',
  // PREVIEW_IN_OFFLINE_EDITING = 'OFFLINE_EDITING_IN_ACTIVE',

  // PREVIEW_IN_DELETED = 'PREVIEW_IN_DELETED',
  // RESTORE_IN_DELETED = 'RESTORE_IN_DELETED',
  // DELETE_IN_DELETED = 'DELETE_IN_DELETED',

  // PREVIEW_IN_DEL = 'PREVIEW_IN_DEL',

  // PREVIEW_IN_PUBLISHED = 'PREVIEW_IN_PUBLISHED',

  // PREVIEW_IN_RELEASE_ING = 'PREVIEW_IN_RELEASE_ING',
  /* ---------------------------------- 新闻按钮 ---------------------------------- */
  /** 待编辑 */
  SET_TO_BE_EDITED = 'SET_TO_BE_EDITED',
  /** 待改写 */
  SET_TO_BE_REWRITE = 'SET_TO_BE_REWRITE',
  /** 撤销编辑 */
  REVOKE_EDIT = 'REVOKE_EDIT',
  /** 撤销改写 */
  REVOKE_REWRITE = 'REVOKE_REWRITE',
  /** 设为待挖掘 */
  SET_TO_BE_EXCAVATED = 'SET_TO_BE_EXCAVATED',
  /** 预挖掘 */
  PRE_EXCAVATE = 'PRE_EXCAVATE',
  /** 完成预挖掘 */
  COMPLETE_EXCAVATE = 'COMPLETED_EXCAVATE',
  /** 标记为已挖掘 */
  MARK_AS_EXCAVATED = 'MARK_AS_EXCAVATED',
  /** 撤销挖掘 */
  REVOKE_EXCAVATE = 'REVOKE_EXCAVATE',
  /** 设为待删除 */
  SET_TO_BE_DELETED = 'SET_TO_BE_DELETED',
  /** 上一篇 */
  PREVIOUS = 'PREVIOUS',
  /** 下一篇 */
  NEXT = 'NEXT',

  /* ------------------------------------------------ 临床结果按钮 ------------------------------------------------ */
  /** 展开分组 */
  EXPAND_GROUP = 'EXPAND_GROUP',
  /** 收起分组 */
  COLLAPSE_GROUP = 'COLLAPSE_GROUP',
  /** 上移 */
  MOVE_UP = 'MOVE_UP',
  /** 下移 */
  MOVE_DOWN = 'MOVE_DOWN',
  /** 编辑终点结果 */
  EDIT_RESULT = 'EDIT_RESULT',

  /* ------------------------------------------------- 按钮扩展 ------------------------------------------------- */
  /** 添加 */
  ADD = 'ADD',
  /** 粘贴 */
  PASTE = 'PASTE',
  /** 批量删除 */
  BATCH_DELETE = 'BATCH_DELETE',
  /** 展开 */
  EXPAND = 'EXPAND',
  /** 折叠 */
  COLLAPSE = 'COLLAPSE',
  /* ------------------------------------------------- 研发状态 ------------------------------------------------- */
  /** 扩增 */
  MULTIPLE = 'MULTIPLE',
  /* -------------------------------------------------- 交易库 ------------------------------------------------- */
  /** 预览交易 */
  PREVIEW_COMPARISON_DEAL = 'PREVIEW_COMPARISON_DEAL',
  /** 预览事件 */
  PREVIEW_COMPARISON_EVENT = 'PREVIEW_COMPARISON_EVENT',
  /* ------------------------------------------------- 转化医学 ------------------------------------------------- */
  /** 更新药物信息 */
  UPDATE_DRUG_INFO = 'UPDATE_DRUG_INFO',
  /** 增加作者机构 */
  ADD_AUTHOR_INSTITUTION = 'ADD_AUTHOR_INSTITUTION',
  /** 新建文献药物 */
  ADD_PAPER_DRUG = 'ADD_PAPER_DRUG',
}

export enum E_TIME_TRUST_CODE {
  INVALID_DATE = 0,
  DAY = 1,
  MONTH = 2,
  MONTH_DAY = 3,
  YEAR = 4,
  YEAR_DAY = 5,
  YEAR_MONTH = 6,
  YEAR_MONTH_DAY = 7,
}

export enum E_TIME_FORMAT {
  DD_MMM_YYYY = 'YYYY-MM-DD',
  DD_MMM_YYYY_HH_MM_SS_UNDERLINE = 'YYYY_MM_DD_HH_mm_ss',
  YYYYMMDD = 'YYYYMMDD',
  DD_MMM_YYYY_HH_MM_SS = 'YYYY-MM-DD HH:mm:ss',
  MMM_YYYY = 'YYYY-MM',
  YYYY = 'YYYY',
  MMM = 'MMM',
}

export enum E_SORT_FIELD {
  DB_CREATED_AT = 'CREATED_AT',
  DB_CREATED_TS = 'created_ts',
  PG_CREATED_AT = 'created_at',

  DB_UPDATED_AT = 'UPDATED_AT',
  DB_UPDATED_TS = 'updated_ts',
  PG_UPDATED_AT = 'updated_at',
  PHS_UPDATED_AT = 'PHS_UPDATED_AT',
  PHS_UPDATED_AT_L = 'phs_updated_at',
  PHS_CREATED_AT = 'PHS_CREATED_AT',
  PHS_CREATED_AT_L = 'phs_created_at',
  PG_UPDATED_BY = 'updated_by',

  PG_TARGET_NAME_EN = 'name_en',
  PG_TARGET_NAME_CN = 'name_cn',

  PG_DRUG_NAME_EN = 'name_en',
  PG_DRUG_NAME_CN = 'name_cn',

  PG_ERROR_NUM = 'check_detail.error_num',
  PG_WARN_NUM = 'check_detail.warn_num',
  PG_CHECK_TIME = 'check_detail.check_time',

  PG_MECHANISM_NAME_EN = 'name_en',

  PG_DISEASE_NAME_EN = 'name_en',
  PG_DISEASE_NAME_CN = 'name_cn',

  DB_TARGET_NAME_EN = 'target_name_en',
  DB_TARGET_NAME_CN = 'target_name_cn',

  DB_TARGET_CHROMOSOMAL_LOCATION = 'CHROMOSOMAL_LOCATION',
  PG_TARGET_CHROMOSOMAL_LOCATION = 'chromosomal_location',

  DB_LOCUS_GROUP = 'LOCUS_GROUP',
  PG_LOCUS_GROUP = 'locus_group',

  DB_LOCUS_TYPE = 'LOCUS_TYPE',
  PG_LOCUS_TYPE = 'locus_type',

  DB_DRUG_NAME_EN = 'drug_name_en',
  DB_DRUG_NAME_CN = 'drug_name_cn',
  DB_DRUG_CAS_NO = 'CAS_NO',
  PG_DRUG_CAS_NO = 'cas_no',

  DB_MECHANISM_NAME_EN = 'MECHANISM_NAME_EN_SORT',
  DB_MECHANISM_NAME_CN = 'MECHANISM_NAME_CN_SORT',

  DB_DISEASE_NAME_EN = 'DISEASE_NAME_EN_SORT',
  DB_DISEASE_NAME_CN = 'DISEASE_NAME_CN_SORT',

  DB_DISAESE_MESH_ID = 'MESH_ID',
  PG_DISEASE_MESH_ID = 'mesh_id',

  DB_GLOBAL_HIGHEST_DEV_STATUS = 'GLOBAL_HIGHEST_DEV_STATUS',
  PG_GLOBAL_HIGHEST_DEV_STATUS = 'global_highest_dev_status',

  DB_GLOBAL_HIGHEST_DEV_STATUS_BEFORE_TERMINATION = 'GLOBAL_HIGHEST_DEV_STATUS_BEFORE_TERMINATION',
  PG_GLOBAL_HIGHEST_DEV_STATUS_BEFORE_TERMINATION = 'global_highest_dev_status_before_termination',

  DB_HIGHEST_DEV_STATUS_CN = 'HIGHEST_DEV_STATUS_CN',
  PG_HIGHEST_DEV_STATUS_CN = 'highest_dev_status_cn',

  DB_HIGHEST_DEV_STATUS_BEFORE_TERMINATION_CN = 'HIGHEST_DEV_STATUS_BEFORE_TERMINATION_CN',
  PG_HIGHEST_DEV_STATUS_BEFORE_TERMINATION_CN = 'highest_dev_status_before_termination_cn',

  DB_FIRST_APPROVED_DATE = 'FIRST_APPROVED_DATE',
  PG_FIRST_APPROVED_DATE = 'first_approved_date',

  DICT_DISPLAY_NAME = 'display_name',
  DICT_NAME_EN = 'name_en',
  DICT_NAME = 'name',
  DICT_ID = 'dic_id',
  DICT_ATC_CODE = 'atc_code',

  DICT_RANK = 'rnk',

  DB_DISPLAY_NAME = 'DISPLAY_NAME',

  DB_ORG_NAME_CN = 'name_cn_keyword',
  PG_ORG_NAME_CN = 'name_cn',

  DB_ORG_NAME_EN = 'name_keyword_lowercase',
  PG_ORG_NAME_EN = 'name_en',

  DB_ORG_UPDATED_AT = 'updated_ts',
  // clinicalTrial related
  DB_CLINICAL_REGISTER_NUMBER = 'REGISTER_NUMBER',
  PG_CLINICAL_REGISTER_NUMBER = 'register_number',
  TIDB_CLINICAL_REGISTER_NUMBER = 'register_number',

  TIDB_CLINICAL_NORMALIZED_PHASE = 'phase_nor_id',

  TIDB_CLINICAL_NORMALIZED_STATUS = 'recruitment_status_name',

  TIDB_CLINICAL_STUDY_FIRST_POSTED_DATE = 'first_posted_date',

  TIDB_CLINICAL_LAST_UPDATE_POSTED_DATE = 'last_update_posted_date',

  // ctr related
  DB_CTR_ID = 'CLINICAL_TRIAL_ID',
  PG_CTR_ID = 'clinical_trial_id',

  TIDB_CTR_PHASE = 'phase_name',

  TIDB_CTR_NORMALIZED_PHASE = 'phase_nor_id',

  TIDB_CTR_RECRUITMENT_STATUS_NAME = 'recruitment_status_name',

  TIDB_CTR_RECRUITMENT_STATUS_NOR = 'recruitment_status_nor_status',

  TIDB_CTR_STUDY_TYPE = 'study_design_study_category',

  TIDB_CTR_INTERVENTION_MODEL = 'study_design_intervention_model',

  TIDB_CTR_ALLOCATION = 'study_design_allocation',

  TIDB_CTR_MASKING = 'study_design_masking',

  TIDB_CTR_LOCATION = 'study_design_location',

  TIDB_CTR_FIRST_SIGN_DATE_INTERNATIONAL = 'first_sign_date_international',

  TIDB_CTR_FIRST_PARTICIPANT_DATE_INTERNATIONAL = 'first_participant_date_international',

  TIDB_CTR_COMPLETION_DATE_INTERNATIONAL = 'completion_date_international',

  TIDB_CTR_FIRST_SIGN_DATE_DOMESTIC = 'first_sign_date_domestic',

  TIDB_CTR_FIRST_PARTICIPANT_DATE_DOMESTIC = 'first_participant_date_domestic',

  TIDB_CTR_COMPLETION_DATE_DOMESTIC = 'completion_date_domestic',

  TIDB_CTR_STUDY_FIRST_POSTED_DATE = 'first_posted_date',

  TIDB_CTR_LAST_UPDATE_POSTED_DATE = 'last_update_posted_date',

  DB_NEWS_TITLE = 'title',
  PG_NEWS_TITLE = 'title',

  DB_NEWS_SUB_TITLE = 'subtitle',
  PG_NEWS_SUB_TITLE = 'subtitle',

  DB_NEWS_POST_TIME = 'post_time',
  PG_NEWS_POST_TIME = 'post_time',

  DB_NEWS_DMP_POST_TIME = 'dmp_post_time',
  PG_NEWS_DMP_POST_TIME = 'dmp_post_time',

  DB_NEWS_AUTHORS = 'authors',
  PG_NEWS_AUTHORS = 'authors',

  DB_NEWS_CRAWL_BY = 'crawl_by',
  PG_NEWS_CRAWL_BY = 'crawl_by',

  DB_DRUG_APPROVAL_FIRST_APPROVAL_DATE = 'first_approval_date',
  PG_DRUG_APPROVAL_FIRST_APPROVAL_DATE = 'first_approval_date.time_ts',

  DB_DRUG_APPROVAL_PRODUCT_APPROVAL_DATE = 'latest_approval_date',
  PG_DRUG_APPROVAL_PRODUCT_APPROVAL_DATE = 'latest_approval_date.time_ts',

  DB_DRUG_APPROVAL_APPL_TYPE = 'appl_type',
  PG_DRUG_APPROVAL_APPL_TYPE = 'appl_type',

  DB_DRUG_APPROVAL_APPL_NO = 'appl_no',
  PG_DRUG_APPROVAL_APPL_NO = 'appl_no',

  DB_DRUG_APPROVAL_TRADE_NAME = 'TRADE_NAME_EN',
  PG_DRUG_APPROVAL_TRADE_NAME = 'trade_name',

  DB_DRUG_APPROVAL_TRADE_NAME_ANNOTATION = 'DRUG_NAME_EN',
  PG_DRUG_APPROVAL_TRADE_NAME_ANNOTATION = 'trade_name',

  DB_DRUG_APPROVAL_ACTIVE_INGREDIENTS = 'ACTIVE_INGREDIENT_EN',
  PG_DRUG_APPROVAL_ACTIVE_INGREDIENTS = 'active_ingredients',

  DB_DRUG_APPROVAL_APPLICANT = 'APPLICANT_NAME_EN',
  PG_DRUG_APPROVAL_APPLICANT = 'applicant',

  DB_DRUG_APPROVAL_APPLICANT_ANNOTATION = 'APPLICANT_COMPANY_NAME',
  PG_DRUG_APPROVAL_APPLICANT_ANNOTATION = 'applicant',

  DB_DRUG_APPROVAL_INDICATION = 'INDICATION_NOR',
  PG_DRUG_APPROVAL_INDICATION = 'indication',

  DB_DRUG_APPROVAL_SUBMISSION_CLASSIFICATION = 'SUBMISSION_CLASSIFICATION_NAME',
  PG_DRUG_APPROVAL_SUBMISSION_CLASSIFICATION = 'submission_classification',

  DB_DRUG_APPROVAL_MARKED_SUBMISSION_CLASSIFICATION = 'SUBMISSION_CLASSIFICATION_NOR',
  PG_DRUG_APPROVAL_MARKED_SUBMISSION_CLASSIFICATION = 'submission_classification.normalized_id',

  DB_DRUG_APPROVAL_REVIEW_PRIORITY = 'REVIEW_PRIORITY',
  PG_DRUG_APPROVAL_REVIEW_PRIORITY = 'review_priority',

  DB_DRUG_APPROVAL_MARKET_STATUS = 'MARKETING_STATUS',
  PG_DRUG_APPROVAL_MARKET_STATUS = 'marketing_status',

  DB_PBDT = 'PBDT_YEARMONTHDAY',
  PG_PBDT = 'pbdt',

  DB_APDT = 'APD_YEARMONTHDAY',
  PG_APDT = 'apdt',

  DB_LABEL_TYPE = 'PHS_LABEL_TYPE',
  PG_LABEL_TYPE = 'curation',

  DB_MANUAL_APPROVAL = 'PHS_MANUAL_APPROVAL',
  PG_MANUAL_APPROVAL = 'manual_approval',
  DB_REPORT_POST_TIME = 'post_time',
  PG_REPORT_POST_TIME = 'post_time',

  PG_USER_CERTIFICATION_CERT_INITIATION_TIME = 'cert_initiation_time',
  PG_USER_CERTIFICATION_CERT_PASS_TIME = 'cert_pass_time',
  PG_USER_LASTEST_OPERATE_TIME = 'user_lastest_operate_time',

  DB_GENERIC = 'GENERIC',
  PG_GENERIC = 'generic',

  DB_BIOSIMILAR = 'BIOSIMILAR',
  PG_BIOSIMILAR = 'biosimilar',

  DB_BIOMARKER_NAME_EN = 'BIOMARKER_NAME_EN_STR',
  DB_OUTCOME_NAME_EN = 'OUTCOME_NAME_EN_STR',

  PG_PIPELINE_TOTAL_CHANGE_TIMES = 'total_change_count',
  PG_PIPELINE_LATEST_CHANGE_TIME = 'latest_change_time',
  PG_PIPELINE_UN_CHECKED_CHANGE_COUNT = 'unchecked_change_count',
  PG_PIPELINE_UN_ACCEPTED_REGISTER_COUNT = 'unaccepted_register_count',
  PG_PIPELINE_LATEST_CHECKED_TIME = 'latest_checked_time',
  PG_PIPELINE_LATEST_ACCEPTED_TIME = 'latest_accepted_time',

  DEAL_EVENT_ID = 'dealEventId',
  DEAL_SUB_EVENT_ID = 'dealSubEventId',
  DEAL_EVENT_TITLE = 'dealEventTitle',
  DEAL_EVENT_TIME = 'dealEventTime',

  DEV_STATUS_UUID = 'uuid',
  DEV_STATUS_DRUG = 'drug_id',
  DEV_STATUS_DISEASE = 'disease_id',
  DEV_STATUS_ORG = 'org_master_entity_id',
  DEV_STATUS_COUNTRY = 'country',
  DEV_STATUS_DEV_STATUS = 'dev_status',
  DEV_STATUS_PHASE_STATUS = 'phase_status',
  DEV_STATUS_PLAN = 'plan',

  TRANSLATIONAL_MEDICINE_ID = 'translational_medicine_id',
  CT_RESULT_ID = 'ct_result_id',
  TITLE = 'title',
  PUB_DT_TS = 'pub_dt_ts',
}

export enum E_SORT_ORDER {
  DESC = 'desc',
  ASC = 'asc',
}

export enum DICTYPENAMES {
  /** 研发状态 */
  DEV_STATUS = 'DEV_STATUS',
  /** 作用方式 */
  DRUG_MODE = 'DRUG_MODE',
  /** 药物类型 */
  DRUG_TYPE = 'DRUG_TYPE',
  /** 终止原因 */
  TERMINATION_REASON = 'TERMINATION_REASON',
  /** 特殊审评 */
  SPECIAL_REVIEW = 'SPECIAL_REVIEW',
  /** 特殊审评 (国家) */
  APPROVAL_COUNTRY_TUPLE = 'APPROVAL_COUNTRY_TUPLE',
  /** 中国药物分类 */
  REGISTERED_CLASSIFICATION_CN = 'REGISTERED_CLASSIFICATION_CN',
  /** 生物药表达体系 */
  EXPRESS_SYSTEM = 'EXPRESS_SYSTEM',
  /** 生物药来源 */
  BIOLOGICAL_DRUG_SOURCE = 'BIOLOGICAL_DRUG_SOURCE',
  /** 专利类型 */
  PATENT_TYPE = 'PATENT_TYPE',
  /** 专利类型来源 */
  PATENT_TYPE_SOURCE = 'PATENT_TYPE_SOURCE',
  /** 国家 */
  COUNTRY = 'COUNTRY',
  /** ATC Code */
  ATC_CODE = 'ATC_CODE',
  /** 剂型 */
  DOSAGE_FORM = 'DOSAGE_FORM',
  /** 给药途径 */
  ROUTE_OF_ADMINISTRATION = 'ROUTE_OF_ADMINISTRATION',
  /** 市场状态 */
  MARKET_STATUS = 'MARKET_STATUS',
  /** 审评优先级 */
  // REVIEW_PRIORITY = 'REVIEW_PRIORITY',
  /** Orphan状态 */
  // ORPHAN_STATUS = 'ORPHAN_STATUS',
  /** 注册分类 */
  SUBMISSION_CLASSIFICATION = 'SUBMISSION_CLASSIFICATION',
  /** 新闻标签 */
  NEWS_CUSTOM_TAG = 'NEWS_CUSTOM_TAG',
  /** NOR 备注 */
  CHECK_NOTE = 'CHECK_NOTE',
  /** 新闻栏目 */
  NEWS_CHANNEL = 'NEWS_CHANNEL',
  /** 链类型 */
  CHAIN_TYPE = 'CHAIN_TYPE',
  /** 适应症限定词 */
  INDICATION_QUALIFIER = 'INDICATION_QUALIFIER',
  /** AI 标签 */
  NEWS_AI_TAG = 'NEWS_AI_TAG',
  /** 抗体类型 */
  DRUG_ANTIBODY_TYPE = 'DRUG_ANTIBODY_TYPE',
  /** 连接子 */
  DRUG_LINKER = 'DRUG_LINKER',
  /** 载荷 */
  DRUG_PAYLOAD = 'DRUG_PAYLOAD',
  /** 点位 */
  DRUG_SITE_NAME = 'DRUG_SITE_NAME',
  /** 疗法类型 */
  CT_THERAPY_TYPE = 'CT_THERAPY_TYPE',
  /** 盲法 */
  CT_MASKING = 'CT_MASKING',
  /** 干预模式 */
  CT_INTERVENTION_MODEL = 'CT_INTERVENTION_MODEL',
  /** 分配模式 */
  CT_ALLOCATION = 'CT_ALLOCATION',
  /** 自评 */
  CT_EVALUATION = 'CT_EVALUATION',
  /** 标注方法 */
  CT_ANNOTATION_METHOD = 'CT_ANNOTATION_METHOD',
  /** 分组类型 */
  CT_GROUP_TYPE = 'CT_GROUP_TYPE',
  /** 结果类型 */
  CT_RESULT_TYPE = 'CT_RESULT_TYPE',
  /** Primary Purpose */
  CT_PRIMARY_PURPOSE = 'CT_PRIMARY_PURPOSE',
  /** Time Perspective */
  CT_TIME_PERSPECTIVE = 'CT_TIME_PERSPECTIVE',
  /** Observation Model */
  CT_OBSERVATIONAL_MODEL = 'CT_OBSERVATIONAL_MODEL',
  /** 技术分类 */
  PATENT_TECHNOLOGY = 'PATENT_TECHNOLOGY',
  /** 交易类型 */
  DRUG_DEAL_TYPE = 'DRUG_DEAL_TYPE',
  /** 交易是否跨境 */
  DRUG_DEAL_REGION = 'DRUG_DEAL_REGION',
  /** 药品交易状态 */
  DRUG_DEAL_STATUS = 'DRUG_DEAL_STATUS',
  /** 来源类型 */
  DATA_SOURCE = 'DATA_SOURCE',
  /** CT_TAG */
  CT_TAG = 'CT_TAG',
  /** SNP_CT_TAG */
  SNP_CT_TAG = 'SNP_CT_TAG',
  /** 生物医药公司类型 */
  ENTITY_PHARM_TYPE = 'ENTITY_PHARM_TYPE',
  /** 主题/标签 */
  TRANSLATIONAL_MEDICINE_SUBJECT = 'TRANSLATIONAL_MEDICINE_SUBJECT',
  /** 终点结果（单位） */
  CT_UNIT_OF_MEASURE = 'CT_UNIT_OF_MEASURE',
  /** 结果离差类型 */
  CT_DISPERSION_TYPE = 'CT_DISPERSION_TYPE',
  /** 参数类型 */
  CT_PARAM_TYPE = 'CT_PARAM_TYPE',
}

export enum DRUG_APPROVAL_DICTYPENAMES {
  /**
   * FDA审批信息
   */
  DOSAGE_FORM = 'DOSAGE_FORM', // 剂型
  ROUTE_OF_ADMINISTRATION = 'ROUTE_OF_ADMINISTRATION', // 给药途径
  MARKET_STATUS = 'MARKET_STATUS', // 市场状态
  REVIEW_PRIORITY = 'REVIEW_PRIORITY', // 审评优先级
  ORPHAN_STATUS = 'ORPHAN_STATUS', // Orphan状态
}

export enum E_DOC_TYPE {
  NEWS = 'news',
  TRIAL = 'clinical_trial',
  PAPER = 'paper',
  PATENT = 'patent',
  DRUG_APPROVAL = 'drug_approval',
  CT_RESULT = 'ct_result',
  DRUG_DEAL = 'drug_deal',
  TRANSLATIONAL_MEDICINE = 'translational_medicine',
}

export enum E_STUDY_STATUS_INT {
  COMPLETED = 120,
  RECRUITING = 90,
  NOT_YET_YECRUITING = 70,
  UNKNOWN_STATUS = 30,
  NDR = 20,
  DISCONTINUED = 10,
  ACTIVE_NOT_RECRUITING = 110,
  ENROLLING_BY_INVITATION = 80,
  AVAILABLE = 60,
  NO_LONGER_AVAILABLE = 50,
  TEMPORARILY_NOT_AVAILABLE = 40,
  APPROVED_FOR_MARKETING = 100,
}

export enum E_STUDY_STATUS {
  COMPLETED = 'Completed',
  RECRUITING = 'Recruiting',
  NOT_YET_YECRUITING = 'Not yet recruiting',
  UNKNOWN_STATUS = 'Unknown Status',
  NDR = 'NDR',
  DISCONTINUED = 'Discontinued',
  ACTIVE_NOT_RECRUITING = 'Active, not recruiting',
  ENROLLING_BY_INVITATION = 'Enrolling by invitation',
  NO_LONGER_AVAILABLE = 'No longer available',
  AVAILABLE = 'Available',
  APPROVED_FOR_MARKETING = 'Approved for marketing',
  TEMPORARILY_NOT_AVAILABLE = 'Temporarily not available',
}
