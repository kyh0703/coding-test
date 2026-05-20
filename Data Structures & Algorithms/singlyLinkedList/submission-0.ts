class ListNode {
    val: number
    next: ListNode | null

    constructor(val: number) {
        this.val = val
        this.next = null
    }
}

class LinkedList {
    private head: ListNode | null
    private tail: ListNode | null
    private length: number

    constructor() {
        this.head = null
        this.tail = null
        this.length = 0
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index: number): number {
        if (index >= this.length) {
            return -1
        }
        let cur = this.head
        for (let i = 0; i < index; i++) {
            cur = cur!.next
        }
        return cur!.val
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val: number): void {
        const node = new ListNode(val)

        node.next = this.head
        this.head = node
        if (this.length === 0) {
            this.tail = node
        }
        this.length++
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val: number): void {
        const node = new ListNode(val)

        if (this.length === 0) {
            this.head = node
            this.tail = node
        } else {
            this.tail.next = node
            this.tail = node
        }

        this.length++
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index: number): boolean {
        if (index >= this.length) return false

        if (index === 0) {
            this.head = this.head.next
            this.length--
            if (this.length === 0) {
                this.tail = null
            }

            return true
        }

        let prev = this.head
        for (let i = 0; i < index - 1; i++) {
            prev = prev!.next
        }

        const target = prev!.next
        prev!.next = target!.next
        if (index === this.length - 1) {
            this.tail = prev
        }
        this.length--
        return true
    }

    /**
     * @return {number[]}
     */
    getValues(): number[] {
        const values: number[] = []
        let cur = this.head

        while (cur != null) {
            values.push(cur.val)
            cur = cur.next
        }

        return values
    }
}