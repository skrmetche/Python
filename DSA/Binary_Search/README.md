🧠 What Is Binary Search?

 Imagine you have number cards laid out like this:

[0, 1, 2, ..., 100] (they are in order — a sorted list)

🎯 The goal is to find the number 73.



❌ The Slow Way:

You start at 0, then 1, then 2…

 That would take a long time if the number is near the end.



✅ The Smart Way — Binary Search:

Binary Search is a fast algorithm to find a number in a sorted list.

 Instead of checking every number one by one, it divides the list in half each time.



🔍 Step-by-Step Example:\



Start between 0 and 100 → Middle is 50

50 < 73 → Too small → Search between 51 and 100

Middle is 75

75 > 73 → Too big → Search between 51 and 74

Middle is 62

62 < 73 → Too small → Search between 63 and 74

Middle is 68

68 < 73 → Too small → Search between 69 and 74

Middle is 71

71 < 73 → Too small → Search between 72 and 74

Middle is 73 🎉 Found it!

You found the number in just 6 smart steps — not 73!




