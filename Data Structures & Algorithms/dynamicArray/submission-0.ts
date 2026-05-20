class DynamicArray {
    private arr: Array<number>
    private size: number
    private capacity: number

    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity: number) {
        this.size = 0
        this.capacity = capacity
        this.arr = new Array(capacity)
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i: number): number {
        if (i < 0 || i >= this.size) {
            throw new Error("Index out of bounds")
        }
        return this.arr[i]
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i: number, n: number): void {
        if ( i < 0 || i >= this.size) {
            throw new Error("Index out of bounds")
        }
        this.arr[i] = n
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n: number): void {
        if (this.size === this.capacity) {
            this.resize()
        }
        this.arr[this.size] = n
        this.size++
    }

    /**
     * @returns {number}
     */
    popback(): number {
        if (this.size === 0) {
            throw new Error("Array is empty")
        }
        const v = this.arr[this.size - 1]
        this.size--
        return v
    }

    /**
     * @returns {void}
     */
    resize(): void {
        this.capacity = this.capacity*2
        const newArr = new Array(this.capacity)
        for (let i = 0; i < this.size; i++) {
            newArr[i] = this.arr[i]
        }
        this.arr = newArr
    }

    /**
     * @returns {number}
     */
    getSize(): number {
        return this.size
    }

    /**
     * @returns {number}
     */
    getCapacity(): number {
        return this.capacity
    }
}
