class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        businessLineCategories = ["electronics", "grocery", "pharmacy", "restaurant"]

        electronicsList = []
        groceryList = []
        pharmacyList = []
        restaurantList = []

        for i, activity in enumerate(isActive):

            if activity is False:
                continue

            if businessLine[i] not in businessLineCategories:
                continue

            if code[i] == "" or not all(char.isalnum() or char == "_" for char in code[i]):
                continue

            if businessLine[i] == "electronics":
                electronicsList.append(code[i])
            if businessLine[i] == "grocery":
                groceryList.append(code[i])
            if businessLine[i] == "pharmacy":
                pharmacyList.append(code[i])
            if businessLine[i] == "restaurant":
                restaurantList.append(code[i])

        return sorted(electronicsList) + sorted(groceryList) + sorted(pharmacyList) + sorted(restaurantList)
