Classfile /home/u/git/last_chance/Intermediate-Code-Generator/java folder/Test.class
  Last modified May 23, 2020; size 360 bytes
  MD5 checksum 45dc95cebd73b5e25c9bfc5880b664dc
  Compiled from "Test.java"
public class Test
  minor version: 0
  major version: 55
  flags: (0x0021) ACC_PUBLIC, ACC_SUPER
  this_class: #4                          // Test
  super_class: #5                         // java/lang/Object
  interfaces: 0, fields: 0, methods: 2, attributes: 1
Constant pool:
   #1 = Methodref          #5.#15         // java/lang/Object."<init>":()V
   #2 = Float              2.5f
   #3 = Float              3.0f
   #4 = Class              #16            // Test
   #5 = Class              #17            // java/lang/Object
   #6 = Utf8               <init>
   #7 = Utf8               ()V
   #8 = Utf8               Code
   #9 = Utf8               LineNumberTable
  #10 = Utf8               main
  #11 = Utf8               ([Ljava/lang/String;)V
  #12 = Utf8               StackMapTable
  #13 = Utf8               SourceFile
  #14 = Utf8               Test.java
  #15 = NameAndType        #6:#7          // "<init>":()V
  #16 = Utf8               Test
  #17 = Utf8               java/lang/Object
{
  public Test();
    descriptor: ()V
    flags: (0x0001) ACC_PUBLIC
    Code:
      stack=1, locals=1, args_size=1
         0: aload_0
         1: invokespecial #1                  // Method java/lang/Object."<init>":()V
         4: return
      LineNumberTable:
        line 2: 0

  public static void main(java.lang.String[]);
    descriptor: ([Ljava/lang/String;)V
    flags: (0x0009) ACC_PUBLIC, ACC_STATIC
    Code:
      stack=3, locals=3, args_size=1
         0: iconst_5
         1: istore_1
         2: iload_1
         3: i2f
         4: iload_1
         5: i2f
         6: ldc           #2                  // float 2.5f
         8: fmul
         9: fadd
        10: fstore_2
        11: fload_2
        12: ldc           #3                  // float 3.0f
        14: fcmpg
        15: ifge          24
        18: bipush        7
        20: istore_1
        21: goto          26
        24: iconst_5
        25: istore_1
        26: iload_1
        27: iconst_5
        28: if_icmpge     38
        31: iload_1
        32: iconst_1
        33: iadd
        34: istore_1
        35: goto          26
        38: return
      LineNumberTable:
        line 6: 0
        line 9: 2
        line 11: 11
        line 12: 18
        line 16: 24
        line 19: 26
        line 21: 31
        line 28: 38
      StackMapTable: number_of_entries = 3
        frame_type = 253 /* append */
          offset_delta = 24
          locals = [ int, float ]
        frame_type = 1 /* same */
        frame_type = 11 /* same */
}
SourceFile: "Test.java"

