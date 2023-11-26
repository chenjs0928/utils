from urllib.parse import quote, unquote, urlencode, urlparse, parse_qs


def url_quote(string: str, encoding: str = 'utf-8') -> str:
    """
    对字符串进行URL编码
    :param encoding:
    :param string:你好
    :return:
            utf-8: %E4%BD%A0%E5%A5%BD
            gbk: %C4%E3%BA%C3
    """
    return quote(string, encoding=encoding)


def url_unquote(string: str, encoding: str = 'utf-8') -> str:
    """
    对字符串进行URL解码
    :param encoding:
    :param string:
    :return:
    """
    return unquote(string, encoding=encoding)


def url_params_dict_to_str(params: dict, doseq: bool = True, is_unquote: bool = True) -> str:
    """
    将一个字典类型的参数转换成查询字符串
    :param params:
    :param is_unquote: 是否需要解码
    :param doseq: 如果doseq为True，则将多个值的查询字符串合并到一个参数中，否则每个值都分别转换为独立的参数
    :return:
    """
    params_str: str = urlencode(params, doseq=doseq)
    if is_unquote:
        params_str = unquote(params_str)
    return params_str


def url_params_str_to_dict(string: str) -> dict[str, list[str]]:
    """
    将查询字符串转成字典
    :param string:
    :return:
    """
    return parse_qs(string)


def get_url_path(url: str):
    """
    获取请求路径
    :param url: 完整的请求URL
    :return:
    """
    return urlparse(url).path


def get_url_query(url):
    """
    获取查询参数
    :param url: 完整的请求URL
    :return:
    """
    return urlparse(url).query
