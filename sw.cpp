#include <sw>
using namespace sw;

void build(Solution &s)
{
    auto &tesseract = s.addTarget<LibraryTarget>("org.sw.demo.tesseract.tesseract", "5.3.0");
    tesseract += Git("https://github.com/tesseract-ocr/tesseract", "5.3.0");

    // Ajoutez les dépendances nécessaires avec des versions spécifiques
    tesseract.Public += "org.sw.demo.danbloomberg.leptonica"_dep;
    tesseract.Public += "org.sw.demo.google.protobuf-3.21.12"_dep;
}