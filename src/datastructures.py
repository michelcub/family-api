
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    id = int
    first_name = ""
    last_name = ""
    age = int
    lucky_numbers = []
    _members = []
    

    def __init__(self,last_name):
        
        self._members =[{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        try:
            if not member["first_name"] or not member["age"] or not member["lucky_numbers"]:
                return ({'message': 'Member should have a data'}),400
            if not member["id"]:
                member["id"] = self._generateId()

            self._members.append(member)
            for check_member in self._members:
                if check_member == member:
                    return ({'message': 'Member added successfully'}),200
        except:
            print("Error adding member")

    def delete_member(self, id):
        try:
            if not id:
                return ({'message': 'Member should have a id'}),400
            for member in self._members:
                if member["id"] == id:
                    self._members.remove(member)
                    return ({'message': 'Member deleted successfully'})
            return ({'message': 'Member not found'})
        except:
            print("Error deleting member")

    def update_member(self, id, member):
        try:
            if not id:
                raise ValueError("Member should have a id")
            if not isinstance(member, dict):
                raise TypeError("Member should be a dictionary")
            if not member["first_name"] or not member["last_name"] or not member["age"] or not member["lucky_numbers"]:
                raise ValueError("Member should have a data")
            for member in self._members:
                if member["id"] == id:
                    member["first_name"] = member["first_name"]
                    member["last_name"] = member["last_name"]
                    member["age"] = member["age"]
                    member["lucky_numbers"] = member["lucky_numbers"]
                    return ({'message': 'Member updated successfully'})
            return ({'message': 'Member not found'})
        except:
            print("Error updating member")

    def get_member(self, id):
        try:
            if not id:
                raise ValueError("Member should have a id")
            for member in self._members:
                if member["id"] == id:
                    return member
            return ({'message': 'Member not found'})
        except:
            print("Error getting member")

    def get_all_members(self):
        return self._members