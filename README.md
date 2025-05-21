# CLASSHUB
🔐 Project Prompt: Secure School Management System (React + Django)
Objective:
Build a highly secure, efficient, and user-friendly school management system using React (frontend) and Django (backend). The system must include role-based access control, user ID creation, mobile/online payments, and barcode-based verification for multiple user roles.
 
👥 User Roles & Functionalities
🔸 Student
•	View staff announcements and communications.
•	View school fees details (percentage paid, balance).
•	Make payments via mobile money or Visa cards.
•	Message other students (secured internal chat).
•	Access downloadable notes and view results.
•	Join online lectures via an integrated video system.
•	Barcode generation for identity and payment verification.
🔸 Teacher
•	Conduct online lectures (live or recorded).
•	Upload marks and notes securely (per specific student).
•	Internal staff communications (hidden from students).
•	Communicate with other teachers.
•	Scan barcodes to verify student payments and IDs.
•	Have personal barcodes proving teacher status.
🔸 Bursar
•	Track school income and expenditures:
o	Fees received, donations, salaries paid, balances, etc.
o	Display both percentage and cash-based figures.
•	Communicate with staff.
•	Send demand notes/invoices to students.
•	Verify student membership/payment via barcode scans.
🔸 Parent
•	View child’s academic and financial records.
•	Make payments (mobile money, Visa cards).
•	Communicate with specific teachers or HM.
•	Hold a scannable membership barcode (for askari verification).
🔸 Board of Directors & Headmaster
•	Full visibility of financial data: income and expenditure.
•	View school-wide analytics and summaries.
•	Send mass or targeted communications to staff/students.
🔸 Askari (Security Guard)
•	Scan barcodes for:
o	Verifying student, teacher, and parent membership.
o	Confirming payment validity.
•	Communicate with staff securely.
 
🔒 Security & Technical Requirements
•	Secure ID generation and authentication for all users.
•	Role-based access control using Django and JWT (or session-based auth).
•	HTTPS, CSRF protection, and input validation.
•	Database encryption for sensitive data (especially payments, marks).
•	Mobile money & card payment gateway integration (e.g., Flutterwave, Paystack, Stripe).
•	Barcode generation and scanning (using a React barcode library + Django integration).
•	Responsive UI for mobile, tablet, and desktop.

![image](https://github.com/user-attachments/assets/a98827c6-4215-43d3-abe8-121caac3a0fe)

