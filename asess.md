> স্কুল মানাজেমেন্ট প্রোজেক্ট

- [ ] Users
  - [ ] Students
  - [ ] Assistant Head Teacher
  - [ ] Committee
  - [ ] Assistant Teacher
  - [ ] Office Assistant
  - [ ] Peon

- [ ] Institute
  - [ ] name
  - [ ] established_year
  - [ ] president
  - [ ] principal
  - [ ] sub_domain
  - [ ] email
  - [ ] address
  - [ ] phone_number_1
  - [ ] phone_number_2
  - [ ] image
  - [ ] logo
  - [ ] description
  - [ ] timestamp
- [ ] Institute Type
  - [ ] institute
  - [ ] eiin_number
  - [ ] institute_code
  - [ ] types
- [ ] Class
  - [ ] name
  - [ ] seats
  - [ ] room_number
- [ ] Subjects
  - [ ] name
  - [ ] code 
  - [ ] option [OPTIONAL, MANDATORY]
  - [ ] type [Primary, Secondary, Hire Secondary, University]
- [ ] Library
- [ ] Attendance
- [ ] Exam
- [ ] Session year
  - [ ] Klass
  - [ ] students []
  - [ ] years
- [ ] Assignment
- [ ] Routine
- [ ] Events
- [ ] Settings
- [ ] Fees

> ইউজার

```
first_name: str
last_name: str
username: str | unique
mobile_number: str | unique
email: str
role: [enum]
```

- [ ] ছাত্র
- [ ] গার্জিয়ান
- [ ] প্রধান শিক্ষক
- [ ] সহকারী প্রধান শিক্ষক
- [ ] সহকারী শিক্ষক
- [ ] দপ্তরি
- [ ] অফিস সহকারী
- [ ] পিয়ন
- [ ] কেরানি

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


