public class Solution {
    public bool IsAnagram(string s, string t) {
        char[] s1 = s.ToCharArray();
        char[] s2 = t.ToCharArray();

        Array.Sort(s1);
        Array.Sort(s2);
        s1.ToList().ForEach(i => Console.WriteLine(i.ToString()));
        s2.ToList().ForEach(i => Console.WriteLine(i.ToString()));


        bool equal = true;
        if(s1.Length != s2.Length)
        return false;
        for(int i = 0; i < s1.Length; i++)
        {
            if (s1[i] != s2[i])
            equal = false;
        }
        if (equal)
        return true;
        else 
        return false;

    }
}
