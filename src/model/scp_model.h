#ifndef SCP_SMARTCALC2_MODEL_H
#define SCP_SMARTCALC2_MODEL_H

#include <cmath>
#include <functional>
#include <iostream>
#include <stack>
#include <unordered_map>
#include <variant>

#include "scp_credit.h"

namespace scp {

class Model {
 public:
  // Main functions
  void ParseExpression(const std::string& expression);
  double Calculate(double x = 0);

  // Bonus functions (credit)
  CreditResult CreditAnnuity(double principal, double term,
                             double interestRate);
  CreditResult CreditDifferentiated(double principal, double term,
                                    double interestRate);

 private:
  // All possible token types, the order is important, because operators '>' '<'
  // are used in conditions
  enum class TokenType : char {
    kNone,
    kNumber,
    kX,
    kOpenParenthesis,
    kCloseParenthesis,
    kDiv,
    kMul,
    kExp,
    kPlus,
    kMinus,
    kMod,
    kSin,
    kCos,
    kTan,
    kAsin,
    kAcos,
    kAtan,
    kSqrt,
    kLn,
    kLog
  };

  using Token = std::variant<double, TokenType>;

  std::vector<Token> rpn_queue_;

  // Message text if an expression is invalid
  static const inline std::string invalid_exp_message_ = "Invalid expression";

  // Basic arithmetic functions
  static double Add(double a, double b) { return a + b; }
  static double Subtract(double a, double b) { return a - b; }
  static double Multiply(double a, double b) { return a * b; }
  static double Divide(double a, double b) {
    if (b == 0) {
      throw std::domain_error("Division by zero");
    }
    return a / b;
  }

  // Maps to parse tokens and handle functions
  static inline std::unordered_map<std::string, TokenType> tokens_map_ = {
      {"(", TokenType::kOpenParenthesis},
      {")", TokenType::kCloseParenthesis},
      {"/", TokenType::kDiv},
      {"*", TokenType::kMul},
      {"^", TokenType::kExp},
      {"+", TokenType::kPlus},
      {"-", TokenType::kMinus},
      {"mod", TokenType::kMod},
      {"cos", TokenType::kCos},
      {"sin", TokenType::kSin},
      {"tan", TokenType::kTan},
      {"acos", TokenType::kAcos},
      {"asin", TokenType::kAsin},
      {"atan", TokenType::kAtan},
      {"sqrt", TokenType::kSqrt},
      {"ln", TokenType::kLn},
      {"log", TokenType::kLog},
      {"x", TokenType::kX},
      {"X", TokenType::kX}};

  static inline std::unordered_map<TokenType, std::function<double(double)>>
      unary_functions_map_ = {
          {TokenType::kSin, static_cast<double (*)(double)>(std::sin)},
          {TokenType::kCos, static_cast<double (*)(double)>(std::cos)},
          {TokenType::kTan, static_cast<double (*)(double)>(std::tan)},
          {TokenType::kAsin, static_cast<double (*)(double)>(std::asin)},
          {TokenType::kAcos, static_cast<double (*)(double)>(std::acos)},
          {TokenType::kAtan, static_cast<double (*)(double)>(std::atan)},
          {TokenType::kSqrt, static_cast<double (*)(double)>(std::sqrt)},
          {TokenType::kLn, static_cast<double (*)(double)>(std::log)},
          {TokenType::kLog, static_cast<double (*)(double)>(std::log10)}};
  static inline std::unordered_map<TokenType,
                                   std::function<double(double, double)>>
      binary_functions_map_ = {
          {TokenType::kPlus, Add},
          {TokenType::kMinus, Subtract},
          {TokenType::kMul, Multiply},
          {TokenType::kDiv, Divide},
          {TokenType::kMod, static_cast<double (*)(double, double)>(std::fmod)},
          {TokenType::kExp, static_cast<double (*)(double, double)>(std::pow)}};

  // Helper functions
  bool IsBinaryOperator(TokenType type);

  bool IsValue(TokenType type);

  bool IsFunction(TokenType type);

  bool IsPlusMinus(TokenType type);

  int GetPriority(TokenType type);

  TokenType GetTokenType(std::string::const_iterator& it,
                         std::string::const_iterator& end);

  bool IsValidToken(TokenType ctt, TokenType ptt);

  void HandleCloseParenthesis(std::stack<Token>& op_stack);

  std::size_t ParseNumber(const std::string& expression);

  void HandleBinaryOperator(std::stack<Token>& op_stack, TokenType ctt,
                            TokenType ptt);

  void MoveOperatorsFromStackToQueue(std::stack<Token>& op_stack);

  bool SkipSpaces(std::string::const_iterator& it,
                  std::string::const_iterator& end);

  void ThrowInvalidExpression();

  void ClearTheQueue();

  double CreditDifferentiatedMonthly(double principal, double term,
                                     double interestRate, int m);
};
}  // namespace scp
#endif  // SCP_SMARTCALC2_MODEL_H