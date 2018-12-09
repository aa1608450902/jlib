#ifndef __STD_API_H__ // standard c++ api
#define __STD_API_H__

/* Part 1. Include file
 */
#include <string>

/* Part 2. Conditional Compilation
 */
#ifdef __cplusplus
// ...
#endif

#if defined(__cplusplus)
// ...
#elif define(__cplusplus)
// ...
#endif


/* Part 3. Macro Definition
 */
#define JUST_FOR_TIPS // Just for reminder

#define emit // MOC compiler processing
#define Q_EMIT

#define Q_OBJECT // ...

#define Q_PROPERTY(...) QT_ANNOTATE_CLASS(qt_property, __VA_ARGS__)

#define offsetof(TYPE, MEMBER) (size_t)&(((TYPE *)0)->MEMBER)

/* Part 4. class decleration
 */
class A;
class B;

class OtherClass;
class AnotherClass;

/* Part 5. class definition
 */
class Meta {
public:
	// Expand functionality by macro and compiler.
	Q_OBJECT

	Q_PROPERTY(int number READ getNumber)

public:
	enum MetaFlag {
		FlagOne = 0x1,
		FlagTwo = 0x2
	}

	explicit Meta(OtherClass *ptr, AnotherClass ins);

	inline string getName() const;

	friend class FriendClass;
	friend void friendFunction(Meta& meta);

protected:
	void doSomething();

private:
	void implement();

private:
	string _clsName;
};

/* Part 6. implementation of some simple function
 */
void friendFunction(Meta& meta) {
	meta._clsName = "cls_meta";
}

// inline function
inline string getName() {
	return _clsName;
}

// non-member function
void setMetaClass(Meta& m) {

}

#endif  /* __STD_API_H__ */
