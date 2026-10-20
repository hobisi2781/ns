class Solution {
    public int countSeniors(String[] details) {
        return (int) Stream
            .of(details)
            .map(d -> Integer.valueOf(d.substring(11, 13)))
            .filter(a -> a > 60)
            .count();
    }
}