from .exceptions import CapsolverError

SUPPORT_TASK_TYPE = [
    "HCaptchaTask",
    "HCaptchaTaskProxyLess",
    "HCaptchaEnterpriseTask",
    "HCaptchaEnterpriseTaskProxyLess",

    "FunCaptchaTask",
    "FunCaptchaTaskProxyLess",

    "GeeTestTask",
    "GeeTestTaskProxyLess",

    "ReCaptchaV2Task",
    "ReCaptchaV2TaskProxyLess",

    "ReCaptchaV2EnterpriseTaskProxyLess",
    "ReCaptchaV2EnterpriseTask",

    "ReCaptchaV3Task",
    "ReCaptchaV3TaskProxyLess",

    "MtCaptchaTask",
    "MtCaptchaTaskProxyLess",

    "DataDomeSliderTask",

    "AntiCloudflareTask",

    "AntiKasadaTask",

    "AntiAkamaiBMPTask",

    "ImageToTextTask",

    "HCaptchaClassification",

    "FunCaptchaClassification",

    "AwsWafClassification",

]


def _format_all_task_type():
    list_types = []
    for i in range(len(SUPPORT_TASK_TYPE)):
        list_types.append(f"{i+1}. {SUPPORT_TASK_TYPE[i]}")
    return "\n".join(list_types)


def check_params(params: dict):
    captcha_type: str = params["type"]
    if params["type"] not in SUPPORT_TASK_TYPE:
        raise CapsolverError(f"Unsupported TaskType {captcha_type}"
                             f"\n support types as follow "
                             f"\n{_format_all_task_type()}")
    captcha_type = captcha_type.lower()
    params_keys = params.keys()

    if "recaptcha" in captcha_type:
        if "websiteURL" not in params_keys:
            raise CapsolverError(f"{captcha_type} websiteURL param")
        if "websiteKey" not in params_keys:
            raise CapsolverError(f"{captcha_type} websiteKey param")

    elif "hcaptcha" in captcha_type:
        if "websiteURL" not in params_keys:
            raise CapsolverError(f"{captcha_type} websiteURL param")
        if "websiteKey" not in params_keys:
            raise CapsolverError(f"{captcha_type} websiteKey param")

    elif "funcaptcha" in captcha_type:
        if "websiteURL" not in params_keys:
            raise CapsolverError(f"{captcha_type} websiteURL param")
        if "websitePublicKey" not in params_keys:
            raise CapsolverError(f"{captcha_type} websitePublicKey param")

    elif "geetesttask" in captcha_type:
        if "gt" not in params_keys:
            raise CapsolverError(f"{captcha_type} need gt param")
        if "challenge" not in params_keys:
            raise CapsolverError(f"{captcha_type} need challenge param")

    elif "datadom" in captcha_type:
        if "proxy" not in params_keys:
            raise CapsolverError(f"{captcha_type} need proxy param")
        if "userAgent" not in params_keys:
            raise CapsolverError(f"{captcha_type} need userAgent")

    elif "anticloudflare" in captcha_type:
        if "metadata" not in params_keys:
            raise CapsolverError(f"{captcha_type} need metadata param")

    elif "antikasada" in captcha_type:
        if "pageURL" not in params_keys:
            raise CapsolverError(f"{captcha_type} need pageURL param")
        if "proxy" not in params_keys:
            raise CapsolverError(f"{captcha_type} need proxy param")

    elif "antiakamaibmp" in captcha_type:
        if "packageName" not in params_keys:
            raise CapsolverError(f"{captcha_type} need packageName param")
