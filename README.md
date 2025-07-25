# MYC_FSE_Django

<img width="6896" height="5180" alt="MYC_FSE_Django architecture excalidraw" src="https://github.com/user-attachments/assets/6fb21c6c-b42e-431a-ac79-c22b631e3eaf" />

Quick notes:
- This setup is not using a dedicated RBACFilter unlike other MYC backends i.e. MYC_FSE_Spring & MYC_FSE_Expressjs. Instead, its delegating the role/permission check to Django framework's pre-existing implementation. 
- There are two permission groups in place namely "investor_group" and "entrepreneur_group" - each having a set of certain permissions. On a successful signup, user is assigned a group and later down the line @permission_required will handle the permission validation. 

Documentation is yet to be completed...  
TODO: Explain working of each and every file, what they do, and how they're connected to each other.

---
## A bit of trivia:
MYC is intended to bridge the gap between investors and early-stage startup founders — especially those in the seed/pre-seed stage — by helping them connect and raise funds more efficiently. 

Currently, the project is in its very early stages, with only the basic authentication and authorization components in place. However, this lays the foundation for future development and room for expansion. 

I'm not sure how many people this project will reach out to, but nonetheless, if it does make its way to you, feel free to send in your PRs and help me out if you can. Your contributions will hold utmost value. 😊


Got any ideas or suggestions? Or want to collaborate with me? Drop me an email at: avicobiz@gmail.com
