public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
         List<List<string>> result = new List<List<string>>();
        bool[] visited = new bool[strs.Length]; // To track already grouped words

        for (int i = 0; i < strs.Length; i++) {
            if (visited[i]) continue;

            List<string> group = new List<string>();
            group.Add(strs[i]);
            visited[i] = true;

            for (int j = i + 1; j < strs.Length; j++) {
                if (visited[j]) continue;

                char[] arr1 = strs[i].ToCharArray();
                char[] arr2 = strs[j].ToCharArray();
                Array.Sort(arr1);
                Array.Sort(arr2);

                bool equal = true;

                if (arr1.Length != arr2.Length) {
                    equal = false;
                } else {
                    for (int k = 0; k < arr1.Length; k++) {
                        if (arr1[k] != arr2[k]) {
                            equal = false;
                            break;
                        }
                    }
                }

                if (equal) {
                    group.Add(strs[j]);
                    visited[j] = true;
                }
            }

            result.Add(group);
        }

        return result;
    
    }
}
