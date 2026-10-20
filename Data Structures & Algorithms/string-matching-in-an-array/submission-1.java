class Solution {
    public List<String> stringMatching(String[] words) {
        Set<String> res = new HashSet<>();

        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words.length; j++) {
                String container = words[j], containee = words[i];
                if (i == j || containee.length() > container.length()) continue;
                // impl for .contains()
                for (int k = 0; k < container.length(); k++) {
                    int m = k, n = 0;
                    while (
                        m < container.length() && 
                        n < containee.length() && 
                        container.charAt(m) == containee.charAt(n)
                    ) {
                        m++;
                        n++;
                    }
                    if (n >= containee.length()) {
                        res.add(containee);
                        break;
                    };
                }
            }
        }

        return new ArrayList<>(res);
    }
}