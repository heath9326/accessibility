from processing.models import AItem

class ATypeProcessor:
    queryset = []

    def __init__(self, url_id: int):
        print("Initializing ATypeProcessor...")
        self.queryset = AItem.objects.filter(url=url_id)

    def process_elements(self):
        print("ATypeProcessor is called...")
        counter = 0
        for element in self.queryset:
            try:
                if "href=" in element.element:
                    counter = counter + 1
                    print(element.element)
                    # Find index of href element
                    # Find all "" in the element
                    # Find check in "" next to htlm is not empty
                    # If it is not empty find  "alt" element
                    # If it is not inlude it in the report
            except Exception as exc:
                print(f"Exception occurred while processing items, exception: '{exc}'")
                continue
        print(f"Total number of elements found {len(self.queryset)}")
        print(f"Total number of elements processed is {counter}")


