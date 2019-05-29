#!/usr/bin/python -t

def lower_bound(nums, val):
    n = len(nums)
    l = 0
    r = n

    while l < r:
        mid = l + (r-l)/2
        if nums[mid] < val:
            l = mid + 1
        else:
            r = mid

    return l

def upper_bound(nums, val):
    n = len(nums)
    l = 0
    r = n

    while l < r:
        mid = l + (r-l)/2
        if nums[mid] > val:
            r = mid
        else:
            l = mid + 1

    return l


#template <class ForwardIterator, class T>
#  ForwardIterator lower_bound (ForwardIterator first, ForwardIterator last, const T& val)
#{
#  ForwardIterator it;
#  iterator_traits<ForwardIterator>::difference_type count, step;
#  count = distance(first,last);
#  while (count>0)
#  {
#    it = first; step=count/2; advance (it,step);
#    if (*it<val) {                 // or: if (comp(*it,val)), for version (2)
#      first=++it;
#      count-=step+1;
#    }
#    else count=step;
#  }
#  return first;
#}


#template <class ForwardIterator, class T>
#  ForwardIterator upper_bound (ForwardIterator first, ForwardIterator last, const T& val)
#{
#  ForwardIterator it;
#  iterator_traits<ForwardIterator>::difference_type count, step;
#  count = std::distance(first,last);
#  while (count>0)
#  {
#    it = first; step=count/2; std::advance (it,step);
#    if (!(val<*it))                 // or: if (!comp(val,*it)), for version (2)
#      { first=++it; count-=step+1;  }
#    else count=step;
#  }
#  return first;
#}

#lower_bound
length = len(citations)
         
        first = 0
        count = length
         
        while count > 0:
            step = count / 2
            mid = first + step
            if citations[mid] < length - mid:
                first = mid + 1
                count -= (step + 1)
            else:
                count = step
         
        return length - first

