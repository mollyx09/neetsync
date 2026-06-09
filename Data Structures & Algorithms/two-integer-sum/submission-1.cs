public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int a=0, b=0, total = 0;
        bool found = false;
        for(int i = 0; i < nums.Length; i++)
        {
            for(int j = i + 1; j < nums.Length ; j++)
            {
                total = nums[i] + nums[j];
                if (total == target) {
                    a = i;
                    b = j;
                    found = true;
                    break;

                }
               
            }
            if (found)
            break;
       
        }
        
        return new int[] {a, b};

    }
}
