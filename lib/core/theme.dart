import 'package:flutter/material.dart';

/// One place for look-and-feel. Class 4 extends this (text theme, component
/// themes, brand identity). Change [seed] and the whole app re-colors.
abstract final class AppTheme {
  static const Color seed = Color(0xFF0B5D7A); // Puget Sound teal

  static ThemeData light() => _build(Brightness.light);

  static ThemeData dark() => _build(Brightness.dark);

  static ThemeData _build(Brightness brightness) {
    final scheme = ColorScheme.fromSeed(
      seedColor: seed,
      brightness: brightness,
    );
    return ThemeData(
      useMaterial3: true,
      colorScheme: scheme,
    );
  }
}
