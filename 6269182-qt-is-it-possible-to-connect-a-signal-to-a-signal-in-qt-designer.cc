#include <iostream>
#include <QtCore/QObject>
#include <QtCore/QString>

class Signaler1 : public QObject {
  Q_OBJECT
 public:
  void Emit(const QString& str) { Forward(str); }

 signals:
  void Forward(const QString& str);
};

class Signaler2 : public QObject {
  Q_OBJECT

 signals:
  void ForwardAgain(const QString& str);
};

class Receiver {
  Q_OBJECT
 public slots:
  void ReceiveString(const QString& str) {
    std::cout << str.toStdString() << std::endl;
  }
};

int main(int argc, char** argv) {
  Signaler1 sig1;
  Signaler1 sig2;
  Receiver receiver;

  QObject::connect(&sig1, SIGNAL(Forward(const QString&)),
                   &sig2, SIGNAL(ForwardAgain(const QString&)));
  QObject::connect(&sig2, SIGNAL(ForwardAgain(const QString&)),
                   &receiver, SLOT(PrintString(const QString&)));

  sig1.Emit("Hello!");

  return 0;
}
