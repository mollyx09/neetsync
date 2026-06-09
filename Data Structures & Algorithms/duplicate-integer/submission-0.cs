public class Solution {
    public bool hasDuplicate(int[] nums) {
        int count = 0;
        foreach (int item in nums)
        {
            count = 0;
            foreach (int num in nums)
            {
                if (item == num)
                count++;
                if (count > 1)
                {
                    return true;
                }
            }
        }
        return false;
    }
}