.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MCClass/i I
	invokestatic MCClass/foo()I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo()I
Label0:
	getstatic MCClass/i I
	iconst_3
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
Label6:
	getstatic MCClass/i I
	ireturn
Label7:
Label5:
	getstatic MCClass/i I
	iconst_1
	iadd
	putstatic MCClass/i I
	invokestatic MCClass/foo()I
	ireturn
Label1:
.limit stack 4
.limit locals 0
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
