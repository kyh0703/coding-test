type DynamicArray struct {
    size int
    capacity int
    arr []int
}

func NewDynamicArray(capacity int) *DynamicArray {
    return &DynamicArray {
        size: 0,
        capacity: capacity,
        arr: make([]int, capacity),
    }
}

func (da *DynamicArray) Get(i int) int {
    if i < 0 || i >= da.size {
        panic("index out of bounds")
    }
    return da.arr[i]
}

func (da *DynamicArray) Set(i int, n int) {
    if i < 0 || i >= da.size {
        panic("index out of bounds")
    }
    da.arr[i] = n
}

func (da *DynamicArray) Pushback(n int) {
    if da.size == da.capacity {
        da.resize()
    }
    da.arr[da.size] = n
    da.size++
}

func (da *DynamicArray) Popback() int {
    if da.size == 0 {
        panic("array is empty")
    }
    v := da.arr[da.size-1]
    da.size--
    return v
}

func (da *DynamicArray) resize() {
    da.capacity = da.capacity * 2
    newArr := make([]int, da.capacity)
    for i := 0; i < da.size; i++ {
        newArr[i] = da.arr[i]
    }
    da.arr = newArr
}

func (da *DynamicArray) GetSize() int {
    return da.size
}

func (da *DynamicArray) GetCapacity() int {
    return da.capacity
}
