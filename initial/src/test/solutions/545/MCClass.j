.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	i2f
	ldc 0.5
	fcmpl
	ifle Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifgt Label3
	iconst_1
	i2f
	ldc 0.5
	fcmpl
	ifgt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label2
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 6
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
