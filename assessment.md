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
- [ ] Institute
  - [ ] name - string
  - [ ] established_year - date
  - [ ] president - string
  - [ ] principal - int
  - [ ] sub_domain - string
  - [ ] email - string
  - [ ] address - string
  - [ ] phone_number_1 - string
  - [ ] phone_number_2 - string
  - [ ] image
  - [ ] logo
  - [ ] description - string
  - [ ] eiin_number - string
  - [ ] institute_code - string
  - [ ] types - enum [primary_school, high_school]

- [ ] Klass
  - [ ] name - string
  - [ ] seats - int
  - [ ] room_number - int
- [ ] Subjects
  - [ ] name - string
  - [ ] code - number
  - [ ] option - enum[OPTIONAL, MANDATORY]
  - [ ] type - enum[primary_school, high_school]
- [ ] Users
    - [ ] unique_id - string
    - [ ] fist_name - string
    - [ ] last_name - string
    - [ ] username - string
    - [ ] email - string
    - [ ] phone_number - string
    - [ ] age - string
    - [ ] gender - enum[MALE, FEMALE, Others]
    - [ ] address - String
    - [ ] role - enum[STUDENT, Guardian, Head Teacher, Assistant Head Teacher, Assistant Teacher]
    - [ ] blood_group - enum[B+, B-, A+, A-,O+,AB+]
    - [ ] status [Active, Inactive]
- [ ] Students Profile
    - [ ] user - int
    - [ ] sessions - enum[]
    - [ ] passport_size_image - string
    - [ ] father_name - string
    - [ ] mother_name - string
    - [ ] father_or_mother_mobile_number - string
    - [ ] badge - string
- [ ] Guardian Profile
    - [ ] user - int
    - [ ] passport_size_image - string
    - [ ] father_name - string
    - [ ] mother_name - string
    - [ ] students - [int, int]
  - [ ] Staff Profile
    - [ ] father_name - string
    - [ ] mother_name - string
    - [ ] passport_size_image - string
    - [ ] subjects - enum[int,int]
    - [ ] grade - string
    - [ ] salary - int
    - [ ] mobile_numbers - string
  - [ ] Committee
  - [ ] Assistant Teacher
  - [ ] Office Assistant
  - [ ] office_staff

- [ ] Degree
  - [ ] teacher_profile - int
  - [ ] choices - enum [SSC, HSC, Honours, Master, PSD, MA, BA]
  - [ ] point - decimal
  - [ ] certificate_image - string 
  - [ ] session_year - date

- [ ] Library
  - [ ] Books
    - [ ] writer_name - string
    - [ ] name - string
    - [ ] cover_image - string
    - [ ] pdf_file - sting
    - [ ] page_number - int
    - [ ] prokasoni_name -  string
- [ ] Attendance
  - [ ] user - int
  - [ ] entry_date_time - time
  - [ ] leave_date_time - time
  - [ ] status - enum[PRESENT, ABSENT]
- [ ] Session year
  - [ ] Klass - int
  - [ ] students - [int, int]
  - [ ] years - number
- [ ] Exam
  - [ ] student - int
  - [ ] exam_type - enum[1st exam, 2 exam, final_exam, test_exam]
  - [ ] session_year - int
  - [ ] fees - int
  - [ ] total_points - decimal
  - [ ] status - enum[FAIL, PASS]
- [ ] Exam Subjects
  - [ ] exam - int
  - [ ] student - int
  - [ ] point - decimal
  - [ ] subject - int
  - [ ] status - enum[ABSEND, PRESENT]
- [ ] Assignment
  - [ ] session_year - int
  - [ ] student - int
  - [ ] subject - int 
  - [ ] lessions - string
  - [ ] point - decimal
  - [ ] teacher - int
  - [ ] status - enum[complete, incomple]
- [ ] Rutine
  - [ ] session_year - int
  - [ ] klass - int
  - [ ] subject - int
  - [ ] time - int
  - [ ] teacher - int
  - [ ] department- enum[generale, since]
- [ ] Events
  - [ ] name - string
  - [ ] banner - string
  - [ ] group_image - string
  - [ ] date - date
  - [ ] bugest - decimal
  - [ ] cost - decimal
- [ ] Fees
  - [ ] choices - enum[exam, event, monthly]
  - [ ] amount - decimal
  - [ ] content_type - int
  - [ ] object_id - int
  - [ ] content_object - enum[content_type, object_id]
  - [ ] status - enum[paid, due]
- [ ] Address
  - [ ] Country - int
  - [ ] Division - int
  - [ ] District - int
  - [ ] sub_district - int
  - [ ] union - int
  - [ ] word - int
  - [ ] moholla - string
  - [ ] house_number - string | null
  - [ ] road_number - string | null

> ছাত্র, শিক্ষক প্রতিদিন হাজিরা
- [ ] ছাত্র, শিক্ষক প্রতিদিন প্রতিষ্ঠানে প্রবেশ করেই হাজিরা দিবেন
- [ ] ছাত্র, শিক্ষক প্রতিদিন প্রতিষ্ঠানে থেকে বের হবার সময় আবার হাজিরা দিতে হবে
- [ ] যদি ছাত্র বা শিক্ষক ১০টার মধ্যে হাজিরা না দেন তাহলে ছাত্রের বেলায় তার গার্জিয়ানের মোবাইল একটা  মেসেজ যাবে আর শিক্ষকের বেলায় অফিস সহকারী বা করতিপক্কর কাছে একটা মেসেজ যাবে আর তার ছাত্রদের কাছে ও একটা মেসেজ যাবে এবং তার পরিবর্তে কে তাদের ক্লাস নিবে সেটা অফিস করতিপক্ষ জানিয়ে দিবেন

> ক্লাস রুম নাম
- [ ] ১ম শ্রেণির
- [ ] ২য় শ্রেণির
- [ ] ৩য় শ্রেণির
- [ ] ৪য় শ্রেণির
- [ ] ৫ম শ্রেণির

> সাবজেক্ট
- [ ] বাংলা
- [ ] ইংরেজি
- [ ] অংক

> সেশন বছর
- [ ] ক্লাসঃ FK
- [ ] সাবজেক্টঃ []
- [ ] ছাত্রঃ []


