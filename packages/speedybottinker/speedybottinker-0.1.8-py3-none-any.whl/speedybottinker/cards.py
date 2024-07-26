from .constants import CONSTANTS
class SpeedyCard:
    def __init__(self):
        self.json = {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.0",
            "body": [],
            "actions": []
        }
        self._stash = {
            "needsSubmit": False,
            "title": "",
            "subTitle": "",
            "chips": [],
            "data": {},
            "submitLabel": "Submit",
        }
        self.id_counter = {}

    def _check_id(self, id=""):
        if id in self.id_counter:
            self.id_counter[id] += 1
            return f"{id}_{self.id_counter[id]}"
        else:
            self.id_counter[id] = 1
            return id

    def needs_submit(self):
        return self._stash["needsSubmit"]

    def add_title(self, title):
        self._stash["title"] = title
        return self

    def add_subtitle(self, subTitle):
        self._stash["subTitle"] = subTitle
        return self

    def add_table(self, input, separator=False):
        facts = []
        if isinstance(input, list):
            facts = [{"title": str(label), "value": str(value)} for label, value in input]
        elif isinstance(input, dict):
            facts = [{"title": str(label), "value": str(value)} for label, value in input.items()]

        payload = {
            "type": "FactSet",
            "separator": separator,
            "facts": facts
        }
        self.json["body"].append(payload)
        return self

    def add_chip(self, payload, id=CONSTANTS["CHIP_LABEL"]):
        return self.add_chips([payload], id)

    def add_chips(self, chips, id="CHIP_LABEL"):
        chip_payload = []
        for chip in chips:
            if isinstance(chip, str):
                chip_payload.append({
                    "type": "Action.Submit",
                    "title": chip,
                    "data": {id: chip}
                })
            elif isinstance(chip, dict):
                title = chip.get("title", "")
                value = chip.get("value", title)
                chip_payload.append({
                    "type": "Action.Submit",
                    "title": title,
                    "data": {id: value}
                })

        if "actions" in self.json:
            self.json["actions"].extend(chip_payload)
        else:
            self.json["actions"] = chip_payload
        return self

    def add_image(self, url, size="ExtraLarge", align="Center", targetURL=None):
        if url:
            payload = {
                "type": "Image",
                "url": url,
                "horizontalAlignment": align,
                "size": size
            }
            if targetURL:
                payload["selectAction"] = {
                    "type": "Action.OpenUrl",
                    "url": targetURL,
                    "style": "positive",
                    "isPrimary": True
                }
            self.json["body"].append(payload)
        return self

    def add_link(self, url, label=None):
        return self.add_text(f"**[{label or url}]({url})**")

    def add_link_button(self, url, label=None):
        clean_id = self._check_id(str(hash(url)))
        payload = {
            "type": "Action.OpenUrl",
            "id": clean_id,
            "title": label or url,
            "url": url
        }
        self.json["actions"].append(payload)
        return self

    def add_text(self, text, bold=False, size="Medium", align="Left", color=None, backgroundColor=None, vertAlign=None):
        payload = {
            "type": "TextBlock",
            "text": text,
            "wrap": True,
            "size": size,
            "horizontalAlignment": align,
            "weight": "Bolder" if bold else "Default",
            **({"color": color} if color else {})
        }

        if backgroundColor or vertAlign:
            container_payload = {
                "type": "Container",
                "height": "stretch",
                "items": [payload],
                **({"style": backgroundColor} if backgroundColor else {}),
                **({"verticalContentAlignment": vertAlign} if vertAlign else {})
            }
            self.json["body"].append(container_payload)
        else:
            self.json["body"].append(payload)
        return self

    def add_header(self, text, config=None):
        if config is None:
            config = {}
        icon_payload = None
        if "iconURL" in config:
            if "http" in config["iconURL"]:
                icon_payload = {
                    "type": "Image",
                    "horizontalAlignment": config.get("iconAlignment", "Left"),
                    "url": config["iconURL"],
                    "width": f'{config.get("iconWidth", 16)}px',
                    **({"style": "person"} if config.get("iconRound") else {})
                }
            else:
                icon_payload = {
                    "type": "Column",
                    "width": "auto",
                    "items": [{
                        "type": "TextBlock",
                        "text": config["iconURL"],
                        "verticalContentAlignment": "Center"
                    }]
                }

        text_payload = {
            "items": [{
                "type": "TextBlock",
                "text": text,
                "wrap": True,
                "size": config.get("textSize", "Large"),
                "horizontalAlignment": config.get("textAlign", "Right" if config.get("rtl") else "Left"),
                **({"color": config["textColor"]} if "textColor" in config else {}),
                **({"style": config["backgroundColor"]} if "backgroundColor" in config else {})
            }]
        }

        columns = [icon_payload, text_payload] if config.get("rtl") else [text_payload, icon_payload]
        columns = [col for col in columns if col is not None]

        header_payload = {
            "type": "ColumnSet",
            "columns": columns
        }

        self._stash["header"] = header_payload
        return self

    def add_block(self, content, backgroundColor=None, vertAlign=None, separator=False):
        if isinstance(content, str):
            return self.add_text(content, backgroundColor=backgroundColor, vertAlign=vertAlign)

        if isinstance(content, SpeedyCard):
            container_payload = {
                "type": "Container",
                "height": "stretch",
                "items": content.build().get("body", []),
                **({"style": backgroundColor} if backgroundColor else {}),
                **({"verticalContentAlignment": vertAlign} if vertAlign else {}),
                **({"separator": separator} if separator else {})
            }
            self._stash["needsSubmit"] = self._stash["needsSubmit"] or content.needs_submit()
            self.json["body"].append(container_payload)
        return self

    def add_subcard(self, card, textLabel=""):
        sub_card = {
            "type": "Action.ShowCard",
            "title": textLabel,
            "card": card.build() if hasattr(card, "build") and callable(card.build) else card
        }
        self.json["actions"].append(sub_card)
        return self

    def add_picker_dropdown(self, choices, id="addPickerDropdown_result"):
        clean_id = self._check_id(id)
        self._stash["needsSubmit"] = True
        formatted_choices = []
        for choice in choices:
            if isinstance(choice, dict):
                formatted_choices.append(choice)
            else:
                formatted_choices.append({
                    "title": str(choice),
                    "value": str(choice)
                })

        payload = {
            "type": "Input.ChoiceSet",
            "id": clean_id,
            "value": "0",
            "isMultiSelect": False,
            "isVisible": True,
            "choices": formatted_choices
        }
        self.json["body"].append(payload)
        return self

    def build(self):
        if 'title' in self._stash:
            self.add_text(f"# {self._stash['title']}", size="ExtraLarge", bold=True)
        if 'subTitle' in self._stash:
            self.add_text(self._stash["subTitle"], size="Large")
        if 'header' in self._stash:
            self.json["body"].insert(0, self._stash["header"])
        return self.json


# Example Usage
if __name__ == "__main__":
    card = SpeedyCard()
    card.add_title("Hello World")
    card.add_subtitle("This is a subtitle")
    card.add_text("This is a simple text block.")
    card.add_image("https://example.com/image.png")
    card.add_link("https://example.com", "Example Link")
    card.add_table([["Label 1", "Value 1"], ["Label 2", "Value 2"]])
    card.add_chip("Chip Example")
    card.add_chip({ "title": "beer", "value": "tapped_this_one"})
    card.add_picker_dropdown(["Option 1", "Option 2", {"title": "Option 3", "value": "3"}])
    
    import json
    print(json.dumps(card.build(), indent=2))


