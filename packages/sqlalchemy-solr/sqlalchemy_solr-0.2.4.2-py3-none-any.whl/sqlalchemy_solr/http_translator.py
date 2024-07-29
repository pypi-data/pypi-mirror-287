class HTTPTranslator:

  def translate(url):

    proto = "http"
    if "use_ssl" in url.query and url.query["use_ssl"] in ["True", "true"]:
      proto = "https"

    if "token" in url.query and url.query["token"] is not None:
      token = url.query["token"]

    local_url = "/" + url.query["database"]
    return f"{proto}{host}:{port}{local_url}"
