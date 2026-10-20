class Solution {
    public boolean isIsomorphic(String s, String t) {
       if (s.length() != t.length()) return false; 
       Map<Character, Character> mapping = new HashMap<>();
       // key from t, and value from s.
       Map<Character, Character> revMapping = new HashMap<>();

       for (int i = 0; i < s.length(); i++) {
            char a = s.charAt(i);
            char b = t.charAt(i);
            if (mapping.containsKey(a) && mapping.get(a) != b) return false;
            if (revMapping.containsKey(b) && revMapping.get(b) != a) return false;
            mapping.put(a, b);
            revMapping.put(b, a);
       }

       return true;
    }
}