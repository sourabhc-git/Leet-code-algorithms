class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

        for(int i = digits.size() - 1; i>=0; i--){

            if ((1 + digits[i]) !=10){
                digits[i] = 1 + digits[i];
                return digits;
            }

            digits[i] = 0;

            if (i == 0){
                    digits.insert(digits.begin(), 1);
                    return digits;
            }
        }
        return digits;
    }
};