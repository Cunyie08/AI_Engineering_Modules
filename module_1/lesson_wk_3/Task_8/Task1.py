# 1. Explain each Output of the program below
nums1 = int(input("Enter first number: "))
nums2 = int(input("Enter second number: "))

nums1 = 3
nums2 = 4

print(f"{nums1} == {nums2} : {nums1 == nums2}") 
# Output is false because the value for the variable (nums1) differs from the value for the variable(nums2), nums1 == nums2 is NOT equal to nums2. 

print(f"{nums1} != {nums2} : {nums1 != nums2}")
# Output is true because the value for the variable (nums1) is NOT equal to the value for the variable(nums2).
 
print(f"{nums1} > {nums2} : {nums1 > nums2}")
# Output is False because the value of the variable (nums1) is not greater than the value of variable (nums2)

print(f"{nums1} < {nums2} : {nums2 < nums1}")
# Output is True because the value of the variable (nums1) is less than the value of variable (nums2)

# 2. State three Cases/Scenarios the above program can be applied
# i. To verify eligibility for Government grants to women in their 50s.
# ii. To check if the result of a medical test conducted for age 35-39 falls within expected range.
# iii. To select qualified Heavyweight boxers to contest for the HWC belt (using their heights).

# 3. Write the code for case (ii)
normal_blood_pressure = 123/82
BP_test_result = 119/84

print(f"Blood Pressure is normal : {normal_blood_pressure == BP_test_result}") # False; result is lower than expected range.
print(f"Blood Pressure is not Normal : {normal_blood_pressure != BP_test_result}") # True; result is lower than normal
print(f"Blood Pressure is higher than expected: {normal_blood_pressure < BP_test_result}") # False; the result is higher than the normal range.
print(f"Blood Pressure is lower than expected: {normal_blood_pressure > BP_test_result}") # True; the result is lower than the normal range.