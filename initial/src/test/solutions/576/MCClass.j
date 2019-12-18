.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo(FF)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	fload_0
	iconst_1
	i2f
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	fload_0
	iconst_0
	i2f
	fcmpl
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iand
	ifgt Label6
	goto Label7
Label6:
	fload_1
	freturn
Label7:
	fload_0
	iconst_1
	i2f
	fsub
	fload_0
	fload_1
	fmul
	invokestatic MCClass/foo(FF)F
	freturn
Label1:
.limit stack 7
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 8
	i2f
	iconst_1
	i2f
	invokestatic MCClass/foo(FF)F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 1
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
