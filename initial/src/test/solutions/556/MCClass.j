.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static fl F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	iconst_1
	isub
	i2f
	iconst_2
	iconst_1
	iadd
	i2f
	ldc 2.5
	iconst_3
	i2f
	fmul
	fdiv
	fsub
	putstatic MCClass/fl F
	getstatic MCClass/fl F
	iconst_2
	i2f
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iconst_0
	invokestatic io/putIntLn(I)V
	goto Label5
Label4:
	getstatic MCClass/fl F
	invokestatic io/putFloatLn(F)V
Label5:
Label1:
	return
.limit stack 4
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
