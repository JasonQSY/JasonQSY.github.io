---
layout: post
title:  "Find the kth Largest Element in an Unsorted Array"
date:   2016-11-12
categories: algorithm
---

The algorithm is motivated by quicksort `partition` function.

## Code by Cpp

    #!cpp
    #include <iostream>

    using namespace std;

    /**
     * the partition function borrowed from quicksort. See also CLRS.
     * time complexity O(n)
     **/
    int partition(int arr[], int left, int right) {
        int x = arr[right];
        int i = left - 1;

        for (int j = left; j < right; j++) {
            if (arr[j] <= x) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        arr[right] = arr[i+1];
        arr[i+1] = x;
        return i + 1;
    }

    /**
     * find the kth largest ele. O(logk) * O(n) = O(nlogk)
     **/
    int find_k(int arr[], int left, int right, int k) {
        int mid = partition(arr, left, right);
        int pos = right - mid + 1;
        if (pos == k) {
            return arr[mid];
        } else if (pos > k) {
            return find_k(arr, mid + 1, right, k);
        } else {
            return find_k(arr, left, mid - 1, k - pos);
        }
    }

    int main() {
        const int M = 10;
        const int K = 2;
        int arr[M] = {6, 4, 9, 12, 18, 13, 5, 1, 3, 10};
        for (int k = 1; k <= M; k++) {
            cout << find_k(arr, 0, M-1, k) << endl;
        }
        //cout << find_k(arr, 0, M - 1, K) << endl;

        return 0;
    }


## Time Complexity

$$N = \Theta(n) \cdot \Theta(\log k) = \Theta(n\log k)$$

However, if the partition always find the max or min element, the algorithm acts the same as an insertion sort whose time whose

$$N = \Theta(nk)$$

since we just sort k elements.
