.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static fl F

.method public static boo()Z
Label0:
	iconst_2
	putstatic MCClass/a I
	getstatic MCClass/a I
	iconst_2
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
	invokestatic MCClass/str()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label5:
	iconst_3
	i2f
	putstatic MCClass/fl F
	invokestatic MCClass/flo()F
	getstatic MCClass/fl F
	fcmpl
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ireturn
Label1:
.limit stack 7
.limit locals 0
.end method

.method public static foo()I
Label0:
	iconst_3
	putstatic MCClass/a I
	getstatic MCClass/a I
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static flo()F
Label0:
	invokestatic MCClass/foo()I
	invokestatic io/putIntLn(I)V
	getstatic MCClass/fl F
	iconst_1
	i2f
	fadd
	freturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/boo()Z
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static str()Ljava/lang/String;
Label0:
	ldc "hello"
	areturn
Label1:
.limit stack 1
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
