import re, warnings
from typing import List, Optional, Union
from typing_extensions import Protocol
from .gakuen_parser import parse_messages, encode_messages
from .story_csv import StoryCsv


class Merger(Protocol):
    def __call__(
        self,
        original_text: str,
        translated_text: str,
        validation_original_text: Optional[str] = None,
        *,
        is_choice: bool = False,
    ) -> str: ...


def gakuen_txt_to_sc_csv(gakuen_txt: str, txt_name_without_ext: str) -> str:
    parsed = parse_messages(gakuen_txt)
    sc_csv = StoryCsv.new_empty_csv(f"{txt_name_without_ext}.txt")
    for line in parsed:
        if line["__tag__"] == "message":
            if line.get("text") is not None and line.get("name") is not None:
                sc_csv.append_line(
                    {
                        "id": "0000000000000",
                        "name": line.get("name"),
                        "text": line.get("text"),
                        "trans": "",
                    }  # type: ignore
                )
        if line["__tag__"] == "choicegroup":
            if isinstance(line["choices"], list):
                for choice in line["choices"]:
                    sc_csv.append_line(
                        {
                            "id": "select",
                            "name": "",
                            "text": choice["text"],
                            "trans": "",
                        }
                    )
            elif isinstance(line["choices"], dict):
                sc_csv.append_line(
                    {
                        "id": "select",
                        "name": "",
                        "text": line["choices"]["text"],
                        "trans": "",
                    }
                )
            else:
                raise ValueError(f"Unknown choice type: {line['choices']}")

    return str(sc_csv)


def trivial_translation_merger(
    original_text: str,
    translated_text: str,
    validation_original_text: Optional[str] = None,
    *,
    is_choice=False,
):
    if (
        validation_original_text is not None
        and validation_original_text != original_text
    ):
        raise ValueError(
            f"Original text does not match validation text: {validation_original_text} != {original_text}"
        )
    return translated_text


# <r\=はなみさき>花海咲季</r>hihihi -> 花海咲季hihihi
def remove_r_elements(input_string):
    pattern = r"<r\\=.*?>(.*?)</r>"
    cleaned_string = re.sub(pattern, r"\1", input_string)
    return cleaned_string


# eg <r\=はなみさき>花海咲季</r>
def line_level_dual_lang_translation_merger(
    original_text: str,
    translated_text: str,
    validation_original_text: Optional[str] = None,
    *,
    is_choice=False,
):
    if (
        validation_original_text is not None
        and validation_original_text != original_text
    ):
        raise ValueError(
            f"Original text does not match validation text: {validation_original_text} != {original_text}"
        )
    if is_choice:
        return f"{original_text}\\n{translated_text}"
    # if line level doesn't match, fallback
    if abs(len(original_text.split("\\n")) - len(translated_text.split("\\n"))) > 1:
        warnings.warn(
            f"Line level doesn't match, fallback to trivial translation merger\nOriginal text: {original_text}\nTranslated text: {translated_text}\n"
        )
        return trivial_translation_merger(
            original_text, translated_text, validation_original_text
        )

    original_text = remove_r_elements(original_text)
    translated_text = remove_r_elements(translated_text)
    if len(original_text.split("\\n")) < len(translated_text.split("\\n")):
        text_len = len(original_text)
        original_text = (
            original_text[0 : text_len // 2] + "\\n" + original_text[text_len // 2 :]
        )
    if len(original_text.split("\\n")) > len(translated_text.split("\\n")):
        original_text = original_text.replace("\\n", " ")
    binds = zip(original_text.split("\\n"), translated_text.split("\\n"))
    texts = []
    for item in binds:
        texts.append(f"<r\\={item[0]}>{item[1]}</r>")
    return "\\n".join(texts)


def merge_translated_csv_into_txt(
    csv_text: Union[str, List[str]],
    gakuen_txt: str,
    merger: Merger,
) -> str:
    story_csv = StoryCsv(csv_text)
    parsed = parse_messages(gakuen_txt)
    iterator = iter(story_csv.data)

    for line in parsed:
        if line["__tag__"] == "message":
            if line.get("text"):
                next_csv_line = next(iterator)
                line["text"] = merger(
                    line["text"], next_csv_line["trans"], next_csv_line["text"]
                )
        if line["__tag__"] == "choicegroup":
            if isinstance(line["choices"], list):
                for choice in line["choices"]:
                    next_csv_line = next(iterator)
                    choice["text"] = merger(
                        choice["text"], next_csv_line["trans"], next_csv_line["text"], is_choice=True
                    )
            elif isinstance(line["choices"], dict):
                next_csv_line = next(iterator)
                line["choices"]["text"] = merger(
                    line["choices"]["text"],
                    next_csv_line["trans"],
                    next_csv_line["text"],
                    is_choice=True,
                )
    return encode_messages(parsed)
