> প্রোজেক্টের নামঃ BD Smart School Management

> Software Requirements Specification

একটা স্কুলের জন্য কিছু পাবলিক এবং প্রাইভেট API তৈরি করতে হবে । আমাদের স্কুলের জন্য শ্রেণি ভেদে user তৈরি করা এবং আমরা প্রতিটি user এর জন্য কিছু গ্রুপ পারমিশন দিয়ে দিবো সেই অনুযায়ী সে কাজ করতে পারবে যদি পারমিশন না দেই তাহলে সে সেই কাজ করতে পারবে না আমাদের user গুলোর টাইপ গুলো যেমনঃ ১। প্রধান শিক্ষক, ২। সহকারী প্রধান শিক্ষক, ৩। সহকারী শিক্ষক ৪। অফিস সহকারী, ৫। স্টাফ, ৬। কমিটি, ৭। ছাত্র, ৮। গার্জিয়ান এবং কিছু grade থাকবে যা আমরা নিজেরা দিবো। ২। ক্লাস থাকবে, ৩। সাবজেক্ট, সাবজেক্টের একটা টাইপ বা স্ট্যাটাস থাকবে যা দিয়ে বুঝাবে সেটা হাই স্কুল নাকি প্রাইমারি স্কুলের জন্য তৈরি করা হচ্ছে, ৪। সেশন বছর তৈরি করার সময় ক্লাস, ছাত্র এবং সাবজেক্ট বলে দিব শুধু সেই সেশনের জন্য, ৫। রুটিন, ৬। পরীক্ষা, ৭। ইভেন্ট, ৮। আসসাইনমেন্ট, ৯। মাসিক বা বাশ্যসরিক বেতন ১০। লাইব্রেরী, লাইব্রেরীতে বই থাকবে বইয়ের জন্য যা যা লাগে যেমন ক। লেখক, খ। প্রকাশনী, গ। বইয়ের  কভার ছবি ঘ। PDF এবং পেইজের নাম্বার আর ও কিছু যুক্ত হতে পারে উপড়ের সব গুলো তৈরি করা থেকে শুরু করে যা যা ফাংশন দরকার পরে সব গুলা API তৈরি করতে হবে প্রয়জনের জন্য আর ও কিছু যুক্ত হতে পারে। আমাদের মাসিক বেতন পরীক্ষা ফি ইত্যাদি কাজ গুলো বাংলাদেশের যেকোনো একটা পেমেন্ট মেথড ব্যাবহার করতে হবে । আমাদের এই Backend সফটওয়ার তা শুধু API বানানোর জন্য আমাদের যেহেতু টাকা পয়সার কাজ আছে আর একটা শিক্ষা প্রতিষ্ঠান সেই জন্য আমাদের সাইবার সিকুরিটি এর বিষয়ে আমাদের বেশি সথরকো থাকতে হবে । এবং অবশই সফটওয়ারটা যেন টেস্টিং করা হয় এবং ডকুমেন্ট থাকতে হবে যেন পরে কেও কাজ করলে তার কোনও সমস্যা না হয়।

1. ফাঙ্কশন রিকয়ারমেন্ট
  1. Authentication
     1. user login mobile number and password or only mobile number and otp not using password
     2. user logout and remove all user data from localhost 
     3. student admission in the school or High school and other all users create admin or our staff
     4. superuser create only one at first
  2. User Management
     1. Chief Teacher or Staff can users
     2. chief Teacher or Staff can see users list and filtering role, mobile number, userID
     3. Chief Teacher or Staff can update and delete users
     4. Chief Teacher or Staff can change user password
  3. institute 
     1. Chief Teacher or Staff can Create institute
     2. Chief Teacher or Staff can institute update and delete
     3. institute see public user
  4. Klass 
     1. Chief Teacher or Staff can Create
     2. Chief Teacher or Staff can update and delete
     3. Chief Teacher or Staff see list and filterin session year wise
     4. klass see public users
  5. Rutine
     1. Chief Teacher or Staff can create
     2. Chief Teacher or Staff update and delete
     3. Chief Teacher or Staff see list and filtering session year 
     4. klass see public users
  6. Events
     1. Chief Teacher or Staff can create
     2. Chief Teacher or Staff can update and delete
     3. Chief Teacher or Staff see list
     4. last 5 or 10 events public see
  7. Assignment
     1. Chief Teacher or Staff can create
     2. Chief Teacher or Staff can update and delete
     3. Chief Teacher or Staff can see list and filtering session year, student and teacher id or mobile number both using for filtering
     4. Teacher add result
  8. Exam
     1. Chief Teacher or Staff can create
     2. Chief Teacher or Staff can update 
     3. Chief Teacher or Staff can see list
     4. exam delete stop every user. it is using for securety purpose
     5. studnet can application for exam and payment after then application approve staff or Chief Teacher
  9. Library
     1.  Chief Teacher or Staff can create
     2.  Chief Teacher or Staff can update
     3.  Chief Teacher or Staff can add books
     4.  Chief Teacher or Staff can update and delete books
     5.  Chief Teacher or Staff can see books list and filtering using fields prokasoni, writer and name

2. কিছু নন ফাঙ্কশনাল প্রয়োজনীয়তা
  ১। password গুলো অবশ্যই hashing অথবা salting টেকনোলোজি ব্যাবহার করতে হবে।
  ২। Security
   ১। API গুলো অবশ্যই secure করার জন্য আপনাকে HTTPS ব্যাবহার করতে হবে
   ২। Authentucation tokens তৈরি করতে হবে এবং চেক করতে হবে সেটা সঠিক কিনা যদি সঠিক না হয় তাহলে আমদের প্রাইভেট API গুলোতে
   Access করতে দিবো না
  ৩। Performance 
    ১। API ফাঙ্কশন গুলো যেন optimize হয় এবং efficient ভাবে কাজ করতে পারে সেটি নিশ্চিত করতে হবে
    ৩। Responsive টাইম যতটা কমানো সম্ভব সেটা নিয়ে কাজ করতে হবে ।
  ৪। Scalability
    ১। আমাদের প্রোজেক্ট তা এমন ভাবে করতে হবে যেকোনো সময় যেন আমরা আমাদের ব্যাবহারকারীর সুবিধার জন্য যেকোনও পদক্ষেপ নিতে পারি 
    যেমনঃ performance এর জন্য যেকোনো একটা বা সব গুলা অ্যাপ যেকোনো সময় আমাদের সার্ভার থেকে আলাদা করতে পারি সেই জন্য সেসব কাজ করতে হবে
    ২। আমাদের সফটওয়ার এর Architecture নিয়ে কাজ করতে হবে যেমনঃ horizontal ও Verticale scalability এবং Load balancing করতে যেন কোনও
    সমস্যা না হয় সেটি নিশ্চিত করতে হবে
    ৩। আমরা এখন রিলেশনাল database ব্যাবহার করলে ও ভবিষ্যতে আমরা যদি আমাদের প্রোজেক্ট microservice এ বিভক্ত করি তখন যেন আমাদের তৈরি করা database এ যেন
    কোনও সমস্যা না হয় ।
  ৫। Reliability
    ১। API গুলো ঠিক ভাবে কাজ করতেছে কিনা সেটা আগে টেস্ট করতে হবে এবং রেসপন্সের এর সময় সঠিক status code ব্যাবহার করতে হবে
    ২। যেকোনো ভুলের জন্য যেন আমাদের প্রোজেক্টের কোনও সমস্যা না হয় সেই জন্য API গুলো অবশ্যই validation করতে হবে ।
৩। Constraints
  ১। BD Smart School Management REST API অ্যাপ্লিকেশনটি তৈরি করতে যেকোনো একটি নির্দিষ্ট প্রোগ্রামিং ভাষা বা framework ব্যবহার করা উচিত।
    যেমনঃ
      languages: nodejs, python
      framework: express, django, flask, fastapi
  ২। এই প্রোজেক্টি সম্পূর্ণ করতে আমাদের thirt-party কিছু package বা লাইব্রেরি ব্যাবহার করতে হতে পারে যেমনঃ
  payment, sms, mail ইত্যাদি 
৪। User Interface
  ১। BD Smart School Management REST API অ্যাপ্লিকেশন, এটি ব্যবহারকারীর জন্য ফ্রন্ট-এন্ড ইন্টারফেস অন্তর্ভুক্ত করা হয়নি. এটি শুধুমাত্র ফ্রন্ট-এন্ড, মোবাইল ও ডেস্কটপ অ্যাপ্লিকেশনের জন্য একটি ব্যাক-এন্ড API প্রদান করে।

১। Entities / Schema / Model
- [x] Institute
  - [x] name - string
  - [x] established_year - date
  - [x] president - string
  - [x] principal - int
  - [x] website_domain_address - string
  - [x] email - string
  - [x] address - string
  - [x] phone_number_1 - string
  - [x] phone_number_2 - string
  - [x] image
  - [x] logo
  - [x] description - string
  - [x] eiin_number - string
  - [x] institute_code - string
  - [x] type - enum [primary_school, high_school]

- [x] Klass
  - [x] institute - int
  - [x] name - string
  - [x] seats - int
  - [x] room_number - int
  - [x] type - enum[primary_school, high_school]
  - [x] timestamp
- [x] Subjects
  - [x] institute - int
  - [x] name - string
  - [x] code - number
  - [x] option - enum[OPTIONAL, MANDATORY]
  - [x] type - enum[primary_school, high_school]
- [x] Users
    - [x] unique_id - string
    - [x] instiute_id - int
    - [x] fist_name - string
    - [x] last_name - string
    - [x] email - string
    - [x] phone_number - string
    - [x] age - string
    - [x] gender - enum[MALE, FEMALE, Others]
    - [x] address - String
    - [x] role - enum[STUDENT, Guardian, Head Teacher, Assistant Head Teacher, Teacher, Assistant Teacher]
    - [x] join_date - datetime
    - [x] login_date - datetime
    - [x] blood_group - enum[B+, B-, A+, A-,O+,AB+]
    - [x] status [Active, Inactive]
    - [x] groups - []
- [x] Students Profile
    - [x] user - int
    - [x] sessions - enum[]
    - [x] passport_size_image - string
    - [x] father_name - string
    - [x] mother_name - string
    - [x] father_or_mother_mobile_number - string
    - [x] badge - string
- [x] Guardian Profile
    - [x] user - int
    - [x] passport_size_image - string
    - [x] father_name - string
    - [x] mother_name - string
    - [x] students - [int, int]
- [x] Staff Profile
  - [x] father_name - string
  - [x] mother_name - string
  - [x] passport_size_image - string
  - [x] subjects - enum[int,int]
  - [x] grade - string
  - [x] salary - int
  - [x] mobile_numbers - string
  - [x] leave_date - date
  - [ ] Committee
  - [ ] Assistant Teacher
  - [ ] Office Assistant
  - [ ] office_staff

- [x] Degree
  - [x] teacher_profile - int
  - [x] choices - enum [SSC, HSC, Honours, Master, PSD, MA, BA]
  - [x] point - decimal
  - [x] certificate_image - string 
  - [x] session_year - date

- [x] Books
  - [x] instittue int
  - [x] writer_name - string
  - [x] name - string
  - [x] cover_image - string
  - [x] pdf_file - sting
  - [x] page_number - int
  - [x] prokasoni_name -  string

- [x] Attendance
  - [x] user - int
  - [x] entry_date_time - time
  - [x] leave_date_time - time
  - [x] status - enum[PRESENT, ABSENT]
- [x] Staff Attendance
  - [x] content_type - int
  - [x] object_id - time
  - [x] object_type - time
  - [x] status - enum[PRESENT, ABSENT]
  - [x] timestamp
- [x] Session year
  - [x] Klass - int
  - [x] students - [int, int]
  - [x] years - number
- [x] Exam
  - [x] students - []
  - [x] exam_type - enum[1st exam, 2 exam, final_exam, test_exam]
  - [x] session_year - int
  - [x] fees - int
  - [x] total_points - decimal
  - [x] status - enum[FAIL, PASS]
- [x] Exam Attendance
  - [x] exam - int
  - [x] student - int
  - [x] point - decimal
  - [x] subject - int
  - [x] status - enum[ABSEND, PRESENT]
- [x] Assignment
  - [x] session_year - int
  - [x] student - int
  - [x] subject - int 
  - [x] lessions - string
  - [x] point - decimal
  - [x] teacher - int
  - [x] status - enum[complete, incomple]
- [x] Rutine
  - [x] session_year - int
  - [x] klass - int
  - [x] subject - int
  - [x] day - enum[sunday, sturday, monday, tuesday,thusday0]
  - [x] time - enum[9am, 10am, 11am, 12pm, 1pm, 2pm, 3pm, 5pm]
  - [x] teacher - int
  - [x] department- enum[generale, since]
  - [x] timestamp
- [x] Events
  - [x] session_year
  - [x] name - string
  - [x] banner - string
  - [x] group_image - string
  - [x] date - date
  - [x] bugest - float
  - [x] cost - float
- [x] Fees
  - [x] choices - enum[exam, event, assignment, monthly]
  - [x] amount - decimal
  - [x] content_type - int
  - [x] object_id - int
  - [x] content_object - enum[content_type, object_id]
  - [x] status - enum[paid, due]
- [x] Address
  - [x] Country - int
  - [x] Division - int
  - [x] District - int
  - [x] sub_district - int
  - [x] union - int
  - [x] word - int
  - [x] moholla - string
  - [x] house_number - string | null
  - [x] road_number - string | null


> routine
> TODO: indivisula routine a multiple teacher add kora jabe and multiple user key abar day select kora jabe jake jedin select kore deya hobe sedin sei teacher class nibe