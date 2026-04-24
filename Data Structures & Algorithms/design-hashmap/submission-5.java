class MyHashMap {
    int[] map;

    public MyHashMap() {
        map=new int[100001];
        for (int i=0;i<100001;i++){
            map[i]=-1;
        }
        
    }
    
    public void put(int key, int value) {
        int index=key%map.length;
        map[index]=value;

        
    }
    
    public int get(int key) {
         int index=key%map.length;
        return map[index];
        
        
    }
    
    public void remove(int key) {
         int index=key%map.length;
        map[index]=-1;
        
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */