class ListNode {
    constructor(val) {
       this.val = val 
       this.next = null
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        if (index < 0 || index >= this.size) return -1;

        let cur = this.head

        for (let i = 0; i < index; i++) {
            cur = cur.next;
        }

        return cur.val;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        const node = new ListNode(val);

        node.next = this.head
        this.head = node

        if (this.size === 0) {
            this.tail = node
        }

        this.size++
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        const node = new ListNode(val);

        if (this.size === 0) {
            this.head = node
            this.tail = node
        } else {
            this.tail.next = node
            this.tail = node
        }

        this.size++
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        if (index < 0 || index >= this.size) return false;

        if (index === 0) {
            this.head = this.head.next
            this.size--

            if (this.size === 0) {
                this.tail = null;
            }
    
            return true
        }

        let prev = this.head
        for (let i = 0; i < index - 1; i++) {
            prev = prev.next
        }

        const target = prev.next
        prev.next = target.next

        if (target === this.tail) {
            this.tail = prev
        }
        
        this.size--;
        return true;
    }

    /**
     * @return {number[]}
     */
    getValues() {
        const values = []
        let cur = this.head

        while (cur) {
            values.push(cur.val)
            cur = cur.next
        }

        return values
    }
}
