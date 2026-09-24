/// Build-time configuration, injected with:
///
///   flutter run --dart-define-from-file=env/dev.json
///
/// SECURITY RULE OF THUMB: anything compiled into the app can be extracted
/// from the APK. Only put low-risk, rate-limited identifiers here. Secrets
/// that must stay secret (e.g. the OneBusAway key) live in `functions/`.
abstract final class AppConfig {
  /// WSDOT Ferries access code (Class 6). Low-risk, but still keep it out of git.
  static const String wsdotAccessCode = String.fromEnvironment(
    'WSDOT_ACCESS_CODE',
  );

  /// Base URL of the Cloud Functions proxy (Class 9), no trailing slash.
  static const String proxyBaseUrl = String.fromEnvironment('PROXY_BASE_URL');

  static bool get hasWsdotCode => wsdotAccessCode.isNotEmpty;
  static bool get hasProxy => proxyBaseUrl.isNotEmpty;
}
