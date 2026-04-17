from .i18n import LANGUAGE_OPTIONS, get_language, get_ui_strings


def ui_i18n(request):
    current_language = get_language(request)
    language_options = [{"code": code, "label": label} for code, label in LANGUAGE_OPTIONS]
    current_language_label = next(
        (option["label"] for option in language_options if option["code"] == current_language),
        current_language.upper(),
    )

    return {
        "current_language": current_language,
        "current_language_label": current_language_label,
        "language_options": language_options,
        "ui": get_ui_strings(current_language),
    }
