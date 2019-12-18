.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	putstatic MCClass/a I
	ldc 2.2
	putstatic MCClass/b F
	getstatic MCClass/a I
	iconst_1
	isub
	i2f
	ldc 3.2
	fmul
	getstatic MCClass/b F
	iconst_3
	i2f
	fadd
	fcmpl
	ifge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBool(Z)V
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
