""" 
roles:
    key: role name
    val: role object
    O(n) space
    Search O(1)
"""

roles = {} 

class Role:
    def __init__(self, role=None) -> None:
        self.role = role
        self.subrole = []
        self.parent = None
        self.user = []
        
class Hierarchy:
    def __init__(self) -> None:
        self.head = None
        
    def createRootRole(self, name: str) -> None:
        r = Role(name)
        self.head = r
        roles[name] = r
        
    def addSubrole(self, name: str, reporting_role: str) -> None:
        
        n = Role(name)
        r = roles[reporting_role]
        
        n.parent = r
        r.subrole.append(n)
        roles[n.role] = n
        
        
    def displayRoles(self) -> None:
        q = []
        q.append(self.head)
        l = []
        while q:
            curr = q.pop(0)
            print(curr.role, end=', ')
            
            if len(curr.subrole):
             
                for s in curr.subrole:
                    q.append(s)
        print()
                
    def delete(self, name: str, role_to_transfer) -> None:
        
        n = roles[name]
        r = roles[role_to_transfer]
        rp = r.parent
        
        n.role = r.role #update name
        
        roles[r.role] = n #update dict
        
        if len(r.user):
            for u in r.user:
                n.user.append(u)
        
        if len(r.subrole):
            for s in r.subrole:
                n.subrole.append(s)
        for i in n.subrole:
            print(i.role)
        rp.subrole.remove(r)
        
    def addUser(self, usr: str, role: str) -> None:
        r = roles[role]
        r.user.append(usr)
        
    def displayUser(self) -> None:
        q = []
        q.append(self.head)
        
        while q:
            curr = q.pop(0)
            
            if len(curr.user):
                for u in curr.user:
                    print(f"{u}- {curr.role}")
                print()
                
            if len(curr.subrole):
                for s in curr.subrole:
                    q.append(s)
            
             
    def displayUserSubuser(self) -> None:
        d={}
        q = []
        q.append(self.head)

        while q:
            curr = q.pop(0)
            d[curr.user[0]] = []
            
            if len(curr.subrole):
                for s in curr.subrole:
                    d[curr.user[0]].append(s.user[0])
                    q.append(s)
            
        for i in d:
            for j in d[i]:
                if str(j) in d:
                    for k in d[j]:
                        if len(k):
                            d[i].append(k) 
        for r in d:
            print(f"{r}- ", end='')
            for u in d[r]:
                print(u, end=', ')
            print()                
                        
    
    def deleteUser(self, name: str) -> None:    
        for r in roles:
            if name in roles[r].user:
                roles[r].user.remove(name)
                    
    def heightUser(self, usr: str) -> int:      
        n_user = 0
        for r in roles:
            if usr in roles[r].user:
                break
        
        ptr = roles[r]    
        
        while ptr.parent:
            n_user += len(ptr.user)
            ptr = ptr.parent
        
        return n_user
    
    def height(self) -> int:
        
        depth = 0
        q = []
        q.append(self.head)
        
        while q:
            depth += 1
            curr = []
            for node in q:
                if len(node.subrole):
                    for s in node.subrole:
                        curr.append(s)
            q = curr
        return depth
    
    def commonBoss(self, usr1: str, usr2: str) -> Role:
        
        for role_name in roles:
            r = roles[role_name]
            
            if usr1 in r.user and usr2 in r.user:
                return r
            if usr1 in r.user:
                u1 = r
            if usr2 in r.user:
                u2 = r
            
        ancestor = set()
        while u1:
            ancestor.add(u1)
            u1 = u1.parent
                
        while u2 not in ancestor:
            u2 = u2.parent
        
        return u2
            
                 
    def getInput(self) -> None:
        root = input("Enter the root role name: ")
        self.createRootRole(root)
        
        while 1:
            print("Operations: ")
            print(" 1. Add Sub Role.\n 2. Display Roles.\n 3. Delete Role.\n 4. Add User.\n 5. Display Users.\n 6. Display Users and Sub Users.\n 7. Delete User.\n 8. Number of users from top.\n 9. Height of role hierarchy.\n 10. Common boss of Users.\n")
            op = int(input())
            
            if op == 1:
                n = input("Enter the sub role name: ")
                r = input("Enter the reporting role name: ") 
                self.addSubrole(name=n, reporting_role=r)
                
            if op == 2:
                self.displayRoles()
                
            if op == 3:
                n = input("Enter the role to be deleted: ")
                r = input("Enter the role to be transferred: ")
                self.delete(name=n, role_to_transfer=r)
                
            if op == 4:
                u = input("Enter User Name: ")
                r = input("Enter Role: ")
                self.addUser(usr=u, role=r)
                
            if op == 5:
                self.displayUser()
            
            if op == 6:
                self.displayUserSubuser()
                
                    
            if op == 7:
                n = input("Enter the username to be deleted: ")
                self.deleteUser(name=n)
                
            if op == 8:
                n = input("Enter the username: ")
                h = self.heightUser(usr=n)
                print(f"Number of users from top: {h}")
                
            if op == 9:
                h = self.height()
                print(f"Height: {h}")
            
            if op == 10:
                u1 = input("Enter the user 1: ")
                u2 = input("Enter the user 2: ")
                r = self.commonBoss(usr1=u1, usr2=u2)
                print(f"Topmost common boss: {r.role}")
            
                
            
              
    
                   
if __name__ == "__main__":      

    h = Hierarchy()
    h.getInput()
      
