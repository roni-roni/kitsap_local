import 'package:flutter/material.dart';

import 'core/theme.dart';
import 'shell/home_shell.dart';

/// Root widget. Class 4 replaces `home:` with a go_router configuration;
/// Class 5 wraps this in a Riverpod `ProviderScope` (in main.dart).
class KitsapApp extends StatelessWidget {
  const KitsapApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Kitsap Local',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.light(),
      darkTheme: AppTheme.dark(),
      themeMode: ThemeMode.system,
      home: const HomeShell(),
    );
  }
}
