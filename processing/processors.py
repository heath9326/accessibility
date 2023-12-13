from processing.models import AItem, FormItem

class ATypeProcessor:
    name = "a_type_elements"
    queryset = []
    key_element_01 = "href="
    key_element_02 = "alt"

    def __init__(self, url_id: int):
        print("Initializing ATypeProcessor...")
        self.queryset = AItem.objects.filter(url=url_id)

    def find_element_quotations(self, element: str):
        pass

    def process_elements(self):
        print("ATypeProcessor is called...")
        counter = 0
        return_elements = []
        for queryset_element in self.queryset:
            try:
                element_text = queryset_element.element
                element_text_list = list(element_text)

                if self.key_element_01 in element_text:
                    counter = counter + 1
                    all_quotes = [i for i in range(len(element_text)) if element_text.startswith('"', i)]
                    href_index = element_text.find(self.key_element_01) + len(self.key_element_01) - 1
                    href_quotations = [index for index in all_quotes if index > href_index][:2]
                    href_link_index = [i for i in range((href_quotations[0] + 1), href_quotations[1])]
                    href_link_text = "".join([element_text[i] for i in href_link_index])
                    is_empty_link = True if not href_link_text or href_link_text == "/" else False
                    if not is_empty_link:
                        has_alt = True if element_text.find(self.key_element_02) > 0 else False
                        if not has_alt:
                            return_elements.append(element_text)
                        else:
                            alt_index = element_text.find(self.key_element_02) + len(self.key_element_02) - 1
                            alt_quotations = [index for index in all_quotes if index > alt_index][:2]
                            alt_link_index = [i for i in range((alt_quotations[0] + 1), alt_quotations[1])]
                            alt_link_text = "".join([element_text[i] for i in alt_link_index])
                            is_empty_link_alt = True if not alt_link_text else False
                            if is_empty_link_alt:
                                return_elements.append(element_text)
                            else:
                                continue
            except Exception as exc:
                print(f"Exception occurred while processing items, exception: '{exc}'")
                continue
        print(f"Total number of elements found {len(self.queryset)}")
        print(f"Total number of elements processed is {counter}")
        return return_elements

class FormTypeProcessor:
    name = "form_elements"
    queryset = []
    key_element_01 = "label"
    key_element_02 = "title"

    def __init__(self, url_id: int):
        print("Initializing FormTypeProcessor...")
        self.queryset = FormItem.objects.filter(url=url_id)

    def find_element_quotations(self, element: str):
        pass

    def process_elements(self):
        print("FormTypeProcessor is called...")
        counter = 0
        return_elements = []
        for queryset_element in self.queryset:
            try:
                element_text = queryset_element.element
                element_text_list = list(element_text)
                if self.key_element_01 not in element_text:
                    return_elements.append(element_text)
                else:
                    if self.key_element_02 not in element_text:
                        return_elements.append(element_text)
                    else:
                        all_quotes = [i for i in range(len(element_text)) if element_text.startswith('"', i)]
                        title_index = element_text.find(self.key_element_02) + len(self.key_element_02) - 1
                        title_quotations = [index for index in all_quotes if index > title_index][:2]
                        href_link_index = [i for i in range((title_quotations[0] + 1), title_quotations[1])]
                        href_link_text = "".join([element_text[i] for i in href_link_index])
                        is_empty_link = True if not href_link_text or href_link_text == "/" else False
                        if not is_empty_link:
                            continue
                        else:
                            return_elements.append(element_text)
            except Exception as exc:
                print(f"Exception occurred while processing items, exception: '{exc}'")
                continue
        print(f"Total number of elements found {len(self.queryset)}")
        print(f"Total number of elements processed is {counter}")
        return return_elements

